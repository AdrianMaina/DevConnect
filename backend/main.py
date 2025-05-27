from fastapi import FastAPI
from backend.routes import jobs, proposals, users
from backend.database import create_tables


app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

# Register routes
app.include_router(jobs.router, prefix="/jobs")
app.include_router(proposals.router, prefix="/proposals")
app.include_router(users.router, prefix="/users")
