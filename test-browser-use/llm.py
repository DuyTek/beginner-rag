from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model_name="claude-3-5-sonnet-latest",
    api_key="",
    temperature=0.0,
    timeout=100
)
