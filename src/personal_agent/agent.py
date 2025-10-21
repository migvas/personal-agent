from pathlib import Path
from dotenv import load_dotenv

from langchain_ollama import ChatOllama

from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchain.messages import HumanMessage

from personal_agent.tools.date_tools import get_current_date
from personal_agent.tools.calendar_tools import get_calendar_meetings
from personal_agent.tools.filesystem_tools import create_file


class PersonalAgent:
    def __init__(self, model: str, temperature: float):
        self.llm = ChatOllama(model=model, temperature=temperature)
        self.tools = self.get_tools()
        self.history = []

        self.agent = create_agent(
            self.llm, tools=self.tools, system_prompt=self.get_system_prompt()
        )

    @classmethod
    def get_agent_graph(cls):
        # Load env vars for graph creation
        load_dotenv(override=True)
        pa = cls("gpt-oss", 0.2)
        return pa.agent

    @staticmethod
    def get_system_prompt():
        path = "./prompts/personal_assistant_prompt.md"
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Prompt file not found: {path}")
        return p.read_text(encoding="utf-8")

    @staticmethod
    def get_tools():
        tools = [get_current_date, get_calendar_meetings, create_file]

        search = DuckDuckGoSearchRun()
        tools.append(search)
        return tools

    def send_message(self, message: str):
        self.history.append(HumanMessage(message))

        resp = self.agent.invoke({"messages": self.history})

        self.history.append(resp["messages"][-1])

        return resp["messages"][-1].content


# Export variable used by langgraph
graph_agent = PersonalAgent.get_agent_graph()
