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
