from fastapi import APIRouter, HTTPException
from src.models import models


router = APIRouter()

@router.post("/")
def create_agent(agent: models.Agent):
    return agent_controller.create_agent_controller(agent)

@router.get("/")
def list_agents():
    return agent_controller.list_agents_controller()

@router.get("/{agent_id}")
def get_agent(agent_id: int):
    return agent_controller.get_agent_controller(agent_id)
