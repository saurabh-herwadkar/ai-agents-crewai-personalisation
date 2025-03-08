# Imports
from crewai import Agent
from textwrap import dedent
from ai_agents_crewai_personalisation.llm.llm_definitions import LLMDefinitions
from ai_agents_crewai_personalisation.tools.tools_definitions import (
    SerperDevTool,
    WebsiteSearchTool,
    secret_code_tool,
)

# Initialise
llm_definitions = LLMDefinitions()
serper_dev_tool = SerperDevTool()
website_search_tool = WebsiteSearchTool()


# Define custom agents
class CustomAgents:

    # Agent defintion
    def agent_1_name(self):
        return Agent(
            role="you are a researcher with good academic experience",
            backstory=dedent(
                f"""You have some good experience in researching topics and fetcing summarized information"""
            ),
            goal=dedent(
                f"""Get 200 words of summarized infromation on the specified topic"""
            ),
            tools=[serper_dev_tool, website_search_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.Ollama,
        )

    # Agent defintion
    def agent_2_name(self):
        return Agent(
            role="you are an expert encrypter",
            backstory=dedent(
                f"""You can create secret hash codes of a text using secret code tools"""
            ),
            goal=dedent(f"""Get a secret code of the 200 words of summarized essay"""),
            tools=[secret_code_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.Ollama,
        )
