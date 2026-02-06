from fastapi import FastAPI
from services.warehouse.routers.routes import router as warehouse_router
from services.gym_assistant.routers.routes import router as gym_router
from services.web_scraper.routers.routes import router as webscraper_router
from services.api_consumption.routers.routes import router as apiconsumption_router
from services.auto_ml.routers.routes import router as auto_ml_router

app = FastAPI()

# -----------------------------
#   ROUTERS
# -----------------------------
app.include_router(warehouse_router, prefix="/warehouse")
app.include_router(gym_router, prefix="/gym")
app.include_router(webscraper_router, prefix="/webscraper")
app.include_router(apiconsumption_router, prefix="/apiconsumption")
app.include_router(auto_ml_router, prefix="/auto-ml")

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