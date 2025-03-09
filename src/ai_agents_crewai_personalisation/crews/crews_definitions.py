# Imports
from crewai import Crew
from ai_agents_crewai_personalisation.agents.agents_definitions import CustomAgents
from ai_agents_crewai_personalisation.tasks.tasks_definitions import CustomTasks

## Initalize
custom_agents = CustomAgents()
custom_tasks = CustomTasks()
custom_agent_1 = custom_agents.content_personalisation_agent()


# Define your crews
class CustomCrews:

    # Crew definitions
    def crew_1_name(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        # Define your custom crew here

        # Variables specific to this crew here here
        description = """
       Save at least 10% for your next getaway at EXPEDIA with TOTUM. Save at least 10% on your next getaway at EXPEDIA! Whether you're planning a city break, beach holiday, or a countryside escape, EXPEDIA has you covered. Book now and enjoy great savings on hotels, flights, and travel packages. Perfect for your next adventure or dream vacation!
        """
        # Capture inputs here if required

        # Return an instance of crew
        return Crew(
            agents=[custom_agent_1],
            tasks=[
                custom_tasks.content_personalisation_task(custom_agent_1, description)
            ],
            verbose=True,
        )
