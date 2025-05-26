from fastapi import APIRouter
from database import get_db_connection

router = APIRouter()

@router.get("/")
def list_jobs():
    conn = get_db_connection()
    jobs = conn.execute("SELECT * FROM jobs").fetchall()
    return [dict(job) for job in jobs]

@router.post("/")
def create_job(job: dict):
    conn = get_db_connection()
    conn.execute(
        '''
        INSERT INTO jobs (title, description, tech_stack, budget, timeline, client_id)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (job['title'], job['description'], job['tech_stack'], job['budget'], job['timeline'], job['client_id'])
    )
    conn.commit()
    return {"message": "Job created successfully"}
