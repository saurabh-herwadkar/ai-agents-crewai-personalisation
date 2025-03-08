# Imports
from crewai import Task
from textwrap import dedent


# Define your tasks here
class CustomTasks:

    # Task definition
    def task_1_name(self, agent, var1):
        return Task(
            description=dedent(
                f"""
            Get some information on the topic. 
            Information should not contain any aggressive or inflammatory content
            Do not use hyperbole or exaggeration
    
            Use this topic: {var1}
            
        """
            ),
            expected_output="Share 200 words on the specified topic as an essay text",
            agent=agent,
        )

    # Task definition
    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
           The previous task will return an essay of 200 words.
           that will be the input text
           use the secret code tool to creat a secret code and share it along with the 200 word essay
            
        """
            ),
            expected_output="Share the secret code and the essay both",
            agent=agent,
        )
