from langgraph.prebuilt import create_react_agent
from app.config.llm import get_llm
from app.config.settings import settings
from app.core.prompt import SYSTEM_PROMPT
from app.core.tools import get_tavily_search
from langchain_core.messages.ai import AIMessage

def get_agent(llm_id=settings.ALLOWED_MODEL_NAMES[0], web_search=False):

    tools = [get_tavily_search()] if web_search else []

    return create_react_agent(
        model=get_llm(llm_id),
        tools=tools,
        prompt=SYSTEM_PROMPT,
    )

def get_agent_response(query, llm_id=settings.ALLOWED_MODEL_NAMES[0], web_search=False):
    agent = get_agent(llm_id=llm_id, web_search=web_search)
    state = {"messages": query}

    response = agent.invoke(state)
    messages = response.get("messages", [])
    if messages:
        ai_message = [msg.content for msg in messages if isinstance(msg, AIMessage)][-1]
        return ai_message
    return ""

if __name__ == "__main__":
    print(get_agent_response("What is the capital of France?"))
