import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from services.gym_assistant import crud
from services.gym_assistant.database import SessionLocal

load_dotenv()

class GymAssistant:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # ============================================================
        #                         PROMPT
        # ============================================================
        self.system_prompt = {
            "role": "system",
            "content": """
            You are a charismatic gym coach AI.

            - ALWAYS reply in the same language the user uses.

            BEHAVIOR:
            - Take initiative when the user greets.
            - Collect fields in this exact order:
            name, age, weight, height, training_days, training_hours, goal, experience.
            - Do NOT call get_user_by_name_and_age until BOTH name and age are known.
            - Once name and age are known → IMMEDIATELY call get_user_by_name_and_age.
            - If the user exists → load their stored data AND show it to the user asking: "Are you this user? (yes/no)". 
            If yes → immediately generate the workout plan.
            - If the user does not exist → collect all fields and then call add_user.
            - After add_user → immediately generate the workout plan.

            RULES:
            - Ask only ONE missing field per message.
            - Never skip the field order.
            - Never ask for a field that is already stored.
            - Never mention tools or functions.
            - Tone must be energetic, friendly, concise.
            """
        }

        # ============================================================
        #                         TOOLS
        # ============================================================
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_user_by_name_and_age",
                    "description": "Get specific user using name + age",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"}
                        },
                        "required": ["name", "age"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "add_user",
                    "description": "Create a new gym user",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"},
                            "weight": {"type": "number"},
                            "height": {"type": "number"},
                            "training_days": {"type": "integer"},
                            "training_hours": {"type": "number"},
                            "goal": {"type": "string"},
                            "experience": {"type": "string"},
                        },
                        "required": [
                            "name","age","weight","height",
                            "training_days","training_hours",
                            "goal","experience"
                        ]
                    }
                }
            }
        ]

    # ============================================================
    #                    SERIALIZER
    # ============================================================
    def to_dict(self, user):
        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "weight": user.weight,
            "height": user.height,
            "training_days": user.training_days,
            "training_hours": user.training_hours,
            "goal": user.goal,
            "experience": user.experience,
        }

    # ============================================================
    #                    RUN ASSISTANT LOGIC
    # ============================================================
    def run(self, conversation):
        messages = [self.system_prompt] + conversation

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=self.tools,
            tool_choice="auto"
        )

        msg = response.choices[0].message

        if msg.tool_calls:
            call = msg.tool_calls[0]
            name = call.function.name
            args = json.loads(call.function.arguments)

            db = SessionLocal()
            
            result = {}

            # ------------------------------
            # execute tool
            # ------------------------------
            if name == "get_user_by_name_and_age":
                user_obj = crud.get_user_by_name_and_age(db, args["name"], args["age"])
                if user_obj:
                    result = self.to_dict(user_obj)
                    #print("DEBUG: user found ->", result)
                    messages.append({
                        "role": "system",
                        "content": f"User found in DB: {json.dumps(result)}"
                    })
                else:
                    result = {}

            elif name == "add_user":
                from services.gym_assistant.schemas import UserCreate
                user_schema = UserCreate(**args)
                created = crud.create_user(db, user_schema)
                result = self.to_dict(created)
                messages.append({
                    "role": "system",
                    "content": f"User created with data: {json.dumps(result)}"
                })

            db.close()

            # ------------------------------
            # return tool result to model
            # ------------------------------
            messages.append({
                "role": "assistant",
                "tool_calls": msg.tool_calls
            })
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": json.dumps(result)  
            })

            # second response
            second = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
)

            return second.choices[0].message.content

        return msg.content
