from fastapi import APIRouter

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response = {"id": summary_id, "url": payload.url}
    return response


@router.get("/{summary_id}/", response_model=SummarySchema)
async def read_summary(summary_id: int) -> SummarySchema:
    summary = await crud.get(summary_id)

    return summary
