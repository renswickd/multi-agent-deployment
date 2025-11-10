from app.config.params import config
from langchain_groq import ChatGroq

def get_llm(model_name=config["model_settings"]["allowed_model_names"][0]):
    return ChatGroq(
        temperature=config["model_settings"]["model_temperature"],
        model=model_name,
        api_key=config["api_keys"]["groq_api_key"],
    )