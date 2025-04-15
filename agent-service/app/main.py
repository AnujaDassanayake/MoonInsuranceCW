from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/agents/", response_model=schemas.Agent)
def create_agent(agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    return crud.create_agent(db, agent)

@app.get("/agents/", response_model=list[schemas.Agent])
def read_agents(db: Session = Depends(get_db)):
    return crud.get_agents(db)

@app.get("/agents/{agent_id}", response_model=schemas.Agent)
def read_agent(agent_id: int, db: Session = Depends(get_db)):
    db_agent = crud.get_agent(db, agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@app.put("/agents/{agent_id}", response_model=schemas.Agent)
def update_agent(agent_id: int, agent: schemas.AgentCreate, db: Session = Depends(get_db)):
    db_agent = crud.update_agent(db, agent_id, agent)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@app.delete("/agents/{agent_id}")
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    if not crud.delete_agent(db, agent_id):
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"message": "Agent deleted successfully"}
