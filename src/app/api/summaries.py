from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response = {"id": summary_id, "url": payload.url}
    return response
