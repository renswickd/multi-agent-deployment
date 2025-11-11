from langchain_tavily import TavilySearch
# from app.config.settings import settings
from app.config.params import config

def get_tavily_search(max_results=config["tavily_config"]["max_results"]):
    return TavilySearch(api_key=config["api_keys"]["tavily_api_key"], 
                        max_results=max_results)