from fastapi import FastAPI
from src.routes import routes

app = FastAPI(title="Pro-1 API", version="0.1.0")

# Root
@app.get("/")
def read_root():
    return {"message": "Hello bro! FastAPI is running!"}

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Include routes (like Express `app.use("/agents", router)`)
app.include_router(routes.router, prefix="/agent", tags=["Agents"])
