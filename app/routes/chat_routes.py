from typing import Optional
from fastapi import APIRouter, HTTPException, Header, Depends
from app.utils.key_pool_request_sender import processor_instance
from ..models.chat_models import ChatRequest
import logging
from app.logger_config import setup_logging

logger = logging.getLogger(__name__)
router = APIRouter()


# 身份验证依赖
async def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        logger.warning("Unauthorized access attempt")
        raise HTTPException(status_code=401, detail="Unauthorized")
    return authorization


async def process_chat_completion(request: ChatRequest):
    try:
        request_body = request.model_dump()
        response = await processor_instance.send_request(request_body)
        return response
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/chat/completions")
async def chat_completions(request: ChatRequest,
                           authorization: str = Depends(verify_token)):
    return await process_chat_completion(request)


@router.post("/v1/chat/completions")
async def chat_completions_v1(request: ChatRequest,
                              authorization: str = Depends(verify_token)):
    return await process_chat_completion(request)
