import requests
import streamlit as st
from app.config.params import load_yaml_config  # Import the function directly
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

config = load_yaml_config()  # Call the function to get the config

BACKEND_HOST = config["urls_and_ports"]["backend_host"]
BACKEND_PORT = config["urls_and_ports"]["backend_port"]
FRONTEND_HOST = config["urls_and_ports"]["frontend_host"]
FRONTEND_PORT = config["urls_and_ports"]["frontend_port"]
BACKEND_BASE_URL = f"http://{BACKEND_HOST}:{BACKEND_PORT}"

logger = get_logger(__name__)

st.set_page_config(
    page_title="Multi Agents App",
    page_icon=":robot_face:"
)

st.title("Multi Agents Deployment - Demo App")

selected_model = st.selectbox("Select Model", config["model_settings"]["allowed_model_names"])
web_search = st.checkbox("🌐 Search")

user_query = st.text_input("Ask a question:")


CHAT_URL = f"{BACKEND_BASE_URL}/api/chat"
print("12345",CHAT_URL)

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
        raise CustomException(f"Error during agent invocation: {e}")