from crewai_tools import SerperDevTool, WebsiteSearchTool
from crewai.tools import tool
import hashlib


@tool("Secret code tool")
def secret_code_tool(input_text: str) -> str:
    """
    This tool is used for generating secret codes for a given text
    the input should be a str

    :param input_text: str, input text for which to retrieve secret code
    :return: str, it returns a secret code which is derived from the input text
    """
    return f"For {input_text} the unique secret code is : {hashlib.md5(input_text.encode()).hexdigest()}"
