from typing import List
from fastapi import APIRouter
from backend.schema import ProposalCreate, ProposalOut
from backend.database import get_db_connection

router = APIRouter(prefix="/proposals", tags=["Proposals"])

@router.get("/", response_model=List[ProposalOut])
def get_all_proposals():
    conn = get_db_connection()
    proposals = conn.execute("SELECT * FROM proposals").fetchall()
    return [dict(p) for p in proposals]

@router.post("/")
def create_proposal(proposal: ProposalCreate):
    conn = get_db_connection()
    conn.execute(
        '''
        INSERT INTO proposals (rate, timeline, message, job_id, freelancer_id)
        VALUES (?, ?, ?, ?, ?)
        ''',
        (proposal.rate, proposal.timeline, proposal.message, proposal.job_id, proposal.freelancer_id)
    )
    conn.commit()
    return {"message": "Proposal submitted successfully"}

