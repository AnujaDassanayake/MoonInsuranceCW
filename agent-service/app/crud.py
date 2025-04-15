from sqlalchemy.orm import Session
from . import models, schemas

def create_agent(db: Session, agent: schemas.AgentCreate):
    db_agent = models.Agent(**agent.dict())
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def get_agent(db: Session, agent_id: int):
    return db.query(models.Agent).filter(models.Agent.id == agent_id).first()

def get_agents(db: Session):
    return db.query(models.Agent).all()

def delete_agent(db: Session, agent_id: int):
    agent = get_agent(db, agent_id)
    if agent:
        db.delete(agent)
        db.commit()
        return True
    return False

def update_agent(db: Session, agent_id: int, updated_agent: schemas.AgentCreate):
    agent = get_agent(db, agent_id)
    if agent:
        for key, value in updated_agent.dict().items():
            setattr(agent, key, value)
        db.commit()
        db.refresh(agent)
        return agent
    return None
