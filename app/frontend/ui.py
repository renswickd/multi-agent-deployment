import requests
import streamlit as st
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(
    page_title="Multi Agents App",
    page_icon=":robot_face:"
)

st.title("Multi Agents Deployment - Demo App")

selected_model = st.selectbox("Select Model", settings.ALLOWED_MODEL_NAMES)
web_search = st.checkbox("🌐 Search")

user_query = st.text_input("Ask a question:")

CHAT_URL = settings.chat_url

if st.button("Submit") and user_query.strip():
    logger.info(
        "Received chat request",
        extra={"llm_name": selected_model,"web_search": web_search}
    )
    payload = {
            "llm_name": selected_model,
            "messages": [user_query],
            "web_search": web_search
        }
    logger.info(f"Payload generated: {payload}")
    try:
        response = requests.post(CHAT_URL, json= payload)

        if response.status_code == 200:
            st.write(response.json())
            logger.info(f"Response Successful: {response.json()}")
        else:
            st.write(f"Error: {response.status_code}")
            logger.info(f"Response Failed: {response.status_code}")

    except Exception as e:
        logger.error(f"Error during agent invocation: {e}")
        st.write(f"Error: {e}")