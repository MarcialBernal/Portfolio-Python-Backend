from fastapi import FastAPI
from services.warehouse.routers.routes import router as warehouse_router
from services.gym_assistant.routers.routes import router as gym_router
from services.web_scraper.routers.routes import router as webscraper_router

app = FastAPI()

# -----------------------------
#   ROUTERS
# -----------------------------
app.include_router(warehouse_router, prefix="/warehouse")
app.include_router(gym_router, prefix="/gym")
app.include_router(webscraper_router, prefix="/webscraper")

# -----------------------------
#   ROOT
# -----------------------------
@app.get("/")
def root():
    return {
        "status": "✅ All services running",
        "services": {
            "🏭 Warehouse": "Online",
            "💪 Gym Assistant": "Online"
        },
        "message": "Backend API operational 🚀"
    }