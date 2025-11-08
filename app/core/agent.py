import asyncio
from langgraph.prebuilt import create_react_agent
from app.config.llm import get_llm
from app.config.settings import settings
from app.core.prompt import SYSTEM_PROMPT
from app.core.tools import get_tavily_search
from app.common.custom_exception import CustomException
from langchain_core.messages.ai import AIMessage

def get_agent(llm_id=settings.ALLOWED_MODEL_NAMES[0], web_search=False):

    tools = [get_tavily_search()] if web_search else []

    return create_react_agent(
        model=get_llm(llm_id),
        tools=tools,
        prompt=SYSTEM_PROMPT,
    )

async def get_agent_response(query, llm_id=settings.ALLOWED_MODEL_NAMES[0], web_search=False):
    agent = get_agent(llm_id=llm_id, web_search=web_search)
    state = {"messages": query}

    try:
        # response = await agent.invoke(state) 
        response = await asyncio.to_thread(agent.invoke, state)

        agent_messages = response.get("messages", [])
        if agent_messages:
            # ai_message_content = [msg.content for msg in agent_messages if hasattr(msg, 'content')][-1]
            ai_message_content = [msg.content for msg in agent_messages if isinstance(msg, AIMessage)][-1]
            return ai_message_content
        
        return "" 

    except Exception as e:
        raise CustomException(f"Error during agent invocation: {e}")

if __name__ == "__main__":
    response = asyncio.run(get_agent_response("What is the capital of France?"))
    print(response)
