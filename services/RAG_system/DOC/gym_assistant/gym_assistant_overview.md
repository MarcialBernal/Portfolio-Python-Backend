# Gym Assistant

## Overview

`gym_assistant` is a FastAPI service that manages gym users and provides a conversational assistant powered by OpenAI.

The assistant collects user fitness information, checks whether the user already exists in the database, creates new users when necessary, and uses function calling to interact with the persistence layer.

## Main Features

- Create, retrieve, update, and delete gym users.
- Search users by name.
- Search users by name and age.
- Store fitness-related information in SQLite.
- Process conversational messages through OpenAI.
- Detect when database operations are required.
- Create new users through OpenAI tool calls.
- Return assistant responses through a FastAPI endpoint.

## User Information

The service stores:

- Name
- Age
- Weight
- Height
- Training days
- Training hours
- Fitness goal
- Experience level
- Creation timestamp

## Assistant Workflow

The assistant follows this process:

1. Receives a conversation through the `/assistant` endpoint.
2. Sends the conversation and system instructions to OpenAI.
3. Determines whether a database function should be called.
4. Searches for an existing user or creates a new user.
5. Sends the database result back to OpenAI.
6. Returns the generated response to the client.

## Persistence

User data is stored in a local SQLite database:

```text
services/gym_assistant/users.db
```

SQLAlchemy is used for database access and ORM model definition.

## API Resources

The service exposes endpoints for:

- User lookup
- User lookup by name and age
- User listing
- User creation
- User update
- User deletion
- Assistant conversations