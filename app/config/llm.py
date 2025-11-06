from app.config.settings import settings
from langchain_groq import ChatGroq

def get_llm(model_name=settings.ALLOWED_MODEL_NAMES[0]):
    return ChatGroq(
        temperature=settings.MODEL_TEMPERATURE,
        model=model_name,
        api_key=settings.GROQ_API_KEY,
    )