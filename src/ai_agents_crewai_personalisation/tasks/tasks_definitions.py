# Imports
from crewai import Task
from textwrap import dedent


# Define your tasks here
class CustomTasks:

    # Task definition
    def content_personalisation_task(self, agent, description):
        return Task(
            description=dedent(
                f"""
            Based on the description provided use the agent to convert it into an offer description 
            Use only llm

            First we need the original deescription as a aprt of the response
            It can be classified under
            description:

            then we need a version of this description for the below 4 social media platforms

            twitter facebook instagram and mobile app push notification
            Use # and similar social emdia best practices wherever applicable

            for each category give an header for example twitter:

            then need a personalised description for 6 categories
            for 10-25 years for 25-50 years and for 50-100 years
            
            both for female and male

            Hence total 18 categories
            For each catgeory give the header as an example 10-25-male , 50-100-female and so on...all small case
            
            
            Use this description: {description}
            
        """
            ),
            expected_output="The original description and Total 10 personalised descriptions for social media platofrms and categories",
            agent=agent,
        )

    
