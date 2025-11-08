from pydantic import BaseModel
from typing import List

class RequestSchema(BaseModel):
    llm_name: str
    messages: str
    web_search: bool