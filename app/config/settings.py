import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def load_yaml_config():
    config_path = Path(__file__).parent / "config.yaml"
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    # Replace environment variables
    config["api_keys"]["groq_api_key"] = os.getenv("GROQ_API_KEY")
    config["api_keys"]["tavily_api_key"] = os.getenv("TAVILY_API_KEY")
    return config

# class Settings:
#     def __init__(self):
#         config = load_yaml_config()
        
#         # API Keys
#         self.GROQ_API_KEY = config["api_keys"]["groq_api_key"]
#         self.TAVILY_API_KEY = config["api_keys"]["tavily_api_key"]

#         # Model Settings
#         self.ALLOWED_MODEL_NAMES = config["model_settings"]["allowed_model_names"]
#         self.MODEL_TEMPERATURE = config["model_settings"]["model_temperature"]
#         self.TOP_K = config["model_settings"]["top_k"]
#         self.DEBUG_KEY = config["model_settings"]["debug_key"]

#         # Tavily Tool Configs
#         self.MAX_RESULTS = config["tavily_config"]["max_results"]

#         # URLs and Ports
#         self.BACKEND_HOST = config["urls_and_ports"]["backend_host"]
#         self.BACKEND_PORT = config["urls_and_ports"]["backend_port"]
#         self.FRONTEND_HOST = config["urls_and_ports"]["frontend_host"]
#         self.FRONTEND_PORT = config["urls_and_ports"]["frontend_port"]

#     @property
#     def backend_base_url(self):
#         return f"http://{self.BACKEND_HOST}:{self.BACKEND_PORT}"

#     @property
#     def frontend_base_url(self):
#         return f"http://{self.FRONTEND_HOST}:{self.FRONTEND_PORT}"

#     @property
#     def chat_url(self):
#         return f"{self.backend_base_url}/api/chat"

# settings = Settings()
