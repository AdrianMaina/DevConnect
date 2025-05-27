from pydantic import BaseModel, EmailStr
from typing import Optional


# -------------------------------
# User Schemas
# -------------------------------

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str  # "client" or "freelancer"


class UserCreate(UserBase):
    pass


class UserOut(UserBase):
    id: int


# -------------------------------
# Job Schemas
# -------------------------------

class JobBase(BaseModel):
    title: str
    description: str
    tech_stack: str  # store as comma-separated string
    budget: int
    timeline: str


class JobCreate(JobBase):
    client_id: int


class JobOut(JobBase):
    id: int
    client_id: int


# -------------------------------
# Proposal Schemas
# -------------------------------

class ProposalBase(BaseModel):
    rate: float
    timeline: str
    message: str


class ProposalCreate(ProposalBase):
    job_id: int
    freelancer_id: int


class ProposalOut(ProposalBase):
    id: int
    job_id: int
    freelancer_id: int
