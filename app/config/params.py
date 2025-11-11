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

config = load_yaml_config()