from fastapi import FastAPI

app = FastAPI(title="Pro-1 API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Hello bro! FastAPI is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}