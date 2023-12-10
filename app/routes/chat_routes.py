from typing import Optional
from fastapi import APIRouter, HTTPException, Header, Depends

from app.utils.key_pool_request_sender import processor_instance
from ..models.chat_models import ChatMessage, ChatRequest, ChatResponse, Choice, Usage
import logging
from app.logger_config import setup_logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/chat/completions")
async def chat_completions(request: ChatRequest,
                           authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")

    # 读取请求主体
    request_body = request.model_dump()

    # 调用异步的 send_request 函数
    response = await processor_instance.send_request(request_body)

    return response
