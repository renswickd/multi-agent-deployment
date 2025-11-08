from langchain_tavily import TavilySearch
from app.config.settings import settings

def get_tavily_search(max_results=settings.MAX_RESULTS):
    return TavilySearch(api_key=settings.TAVILY_API_KEY, 
                        max_results=max_results)