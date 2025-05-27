from typing import List
from fastapi import APIRouter
from backend.schema import UserCreate, UserOut
from backend.database import get_db_connection

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=List[UserOut])
def get_all_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    return [dict(user) for user in users]

@router.post("/")
def create_user(user: UserCreate):
    conn = get_db_connection()
    conn.execute(
        '''
        INSERT INTO users (name, email, role)
        VALUES (?, ?, ?)
        ''',
        (user.name, user.email, user.role)
    )
    conn.commit()
    return {"message": "User created successfully"}
