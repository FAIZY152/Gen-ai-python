from fastapi import APIRouter, HTTPException
from src.models import Agent

router = APIRouter()

@router.post("/agents/")
def create_agent(agent: Agent):
    # Logic to create an agent
    return {"message": f"Agent {agent.name} created successfully"}

