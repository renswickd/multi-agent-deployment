from fastapi import FastAPI, APIRouter, Request, HTTPException
from typing import Dict
from app.backend.schema import RequestSchema
from app.core.agent import get_agent_response
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

router = APIRouter()

@router.post("/chat", response_model=Dict)
async def chat_endpoint(request_data: RequestSchema, http_request: Request):
    # Use structured logging to easily filter/search logs later
    logger.info(
        "Received chat request",
        extra={
            "model_name": request_data.model_name,
            "allow_search": request_data.allow_search,
            "client_ip": http_request.client.host if http_request.client else "N/A"
        }
    )

    # Use dependency injection or global settings for configuration checks
    if request_data.model_name not in settings.ALLOWED_MODEL_NAMES:
        # Use a client-error log level (WARNING/ERROR)
        logger.warning(
            "Invalid model name provided",
            extra={
                "requested_model": request_data.model_name,
                "allowed_models": settings.ALLOWED_MODEL_NAMES
            }
        )
        raise HTTPException(
            status_code=400, 
            detail="Selected Model is out of provided lists"
        )
    
    try:
        response = await get_agent_response(
            request_data.model_name,
            request_data.messages,
            request_data.allow_search,
            request_data.system_prompt
        )
        logger.info("AI response generated successfully")
        return {"response": response}

    except Exception as e:
        # Catch all other unexpected errors
        logger.exception("An unhandled error occurred during AI response generation")
        raise HTTPException(
            status_code=500, 
            detail="An internal server error occurred"
        )