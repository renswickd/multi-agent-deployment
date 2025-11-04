from langgraph.prebuilt import create_react_agent
from config.llm import get_llm
from config.settings import settings
from core.prompt import SYSTEM_PROMPT
from core.tools import get_tavily_search
from langchain_core.messages.ai import AIMessage

def get_agent(llm_id=settings.ALLOWED_MODEL_NAMES[0], web_search=False):

    tools = [get_tavily_search()] if web_search else []

    return create_react_agent(
        llm=get_llm(llm_id),
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

def get_agent_response(query):
    agent = get_agent()
    state = {"messages": query}

    response = agent.invoke(state)
    messages = response.get("messages", [])
    if messages:
        ai_message = [msg.content for msg in messages if isinstance(msg, AIMessage)][-1]
        return ai_message
    return ""
