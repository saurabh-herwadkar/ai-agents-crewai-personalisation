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
    def content_personalisation_agent(self):
        return Agent(
            role="you are a content personalisation expert",
            backstory=dedent(
                f"""You have some good experience in creating personalised offer content based on the demographic and contextual information provided"""
            ),
            goal=dedent(
                f"""Convert the supplied offer information into an attractive offer description based on the demographic and contextual information provided give maximum 100 words"""
            ),
            #tools=[serper_dev_tool, website_search_tool],
            allow_delegation=False,
            verbose=True,
            llm=llm_definitions.OpenAIGPT4,
        )
