from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES =[
        "openai/gpt-oss-120b",
        "llama-3.3-70b-versatile",
        "deepseek-r1-distill-llama-70b"
    ]

    MODEL_TEMPERATURE = 0
    TOP_K = 10

    # Tavily Tool Configs
    MAX_RESULTS = 3

    # backend
    backend_base_url = "http://127.0.0.1:8000"
    chat_url = f"{backend_base_url}/api/chat"

    #frontend
    frontend_base_url = "http://127.0.0.1:8501"


settings=Settings()
