from langchain_tavily import TavilySearch
from config.settings import settings

def get_tavily_search():
    return TavilySearch(api_key=settings.TAVILY_API_KEY, 
                        max_results=settings.MAX_RESULTS)