# Imports
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()
from ai_agents_crewai_personalisation.crews.crews_definitions import CustomCrews
import logging

# Load Agent ops
import agentops

agentops.init()

# Set logging level
logging.getLogger().setLevel(logging.INFO)

# Initalize
custom_crew = CustomCrews()


# The main program to run
# Your crews related code will come here
def run():

    logging.info("--------Entering main method--------------")
    crew_1 = custom_crew.crew_1_name()
    result = crew_1.kickoff()
    logging.info("---------Leaving main method------------")
    return result
