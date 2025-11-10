from fastapi import APIRouter, Request, HTTPException
from typing import Dict
from app.backend.schema import RequestSchema
from app.core.agent import get_agent_response
from app.config.params import config
from app.common.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()

@router.post("/chat", response_model=Dict)
async def chat_endpoint(request_data: RequestSchema, http_request: Request):
    logger.info(
        "Received chat request",
        extra={
            "llm_name": request_data.llm_name,
            "web_search": request_data.web_search,
            "client_ip": http_request.client.host if http_request.client else "N/A"
        }
    )

    if request_data.llm_name not in config["model_settings"]["allowed_model_names"]:
        logger.warning(
            "Invalid model name provided",
            extra={
                "requested_model": request_data.llm_name,
                "allowed_models": config["model_settings"]["allowed_model_names"]
            }
        )
        raise HTTPException(
            status_code=400, 
            detail="Selected Model is out of provided lists"
        )
    
    try:
        response = await get_agent_response(
            llm_id=request_data.llm_name,
            query=request_data.messages,
            web_search=request_data.web_search
        )
        logger.info("AI response generated successfully")
        return {"response": response}

    except Exception as e:
        logger.exception(f"An unhandled error occurred during AI response generation: {e}")
        raise HTTPException(
            status_code=500, 
            detail="An internal server error occurred"
        )