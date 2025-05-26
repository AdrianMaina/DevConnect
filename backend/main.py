from fastapi import FastAPI
from routes import jobs, proposals, users
from fastapi import FastAPI
from routes import jobs, proposals, users  # only if you've created them
from database import create_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()

# Register routes
app.include_router(jobs.router, prefix="/jobs")
# You can comment out proposals and users if not implemented yet
