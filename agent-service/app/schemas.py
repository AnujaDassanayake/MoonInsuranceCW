from pydantic import BaseModel

class AgentBase(BaseModel):
    code: str
    name: str
    email: str
    product: str

class AgentCreate(AgentBase):
    pass

class Agent(AgentBase):
    id: int

    class Config:
        orm_mode = True
