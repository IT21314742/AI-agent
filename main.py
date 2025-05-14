from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv


## Langchain is high level framework that allows us to build ai applications

load_dotenv()

def main():
