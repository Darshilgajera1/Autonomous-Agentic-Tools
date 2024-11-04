from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain_community.chat_models import ChatOpenAI, ChatOllama
# from langchain_ollama import OllamaLLM
from prompt import TOOL_MAKER_PROMPT
from main import MainAgentWithTools

import util
from langchain.tools import Tool
from langchain.agents.agent_toolkits import FileManagementToolkit

from langchain.utilities import GoogleSearchAPIWrapper

from tools.toolRegistration import tool_registration_tool, query_available_modules
from tools.queryTool import tool_query_tool
from tools.browsingTool import paged_web_browser
from tools.liabraryInstallation import verify_and_install_library

util.load_secrets()

# Define system prompts for our agent
system_prompt_scribe = TOOL_MAKER_PROMPT

# initialize file management tools
file_tools = FileManagementToolkit(
    selected_tools=["read_file", "write_file", "list_directory", "copy_file", "move_file", "file_delete"]
).get_tools()


# initialie search API
search = GoogleSearchAPIWrapper()

def top10_results(query):
    return search.results(query, 10)

GoogleSearchTool = Tool(
    name="Google Search",
    description="Search Google for recent results.",
    func=top10_results,
)

tools = [GoogleSearchTool,
         tool_query_tool,
         tool_registration_tool,
         query_available_modules,
         paged_web_browser,
         verify_and_install_library,
         ] + file_tools

# Initialize our agents with their respective roles and system prompts
tool_making_agent = MainAgentWithTools(name="ToolCreator",
                                           system_message=system_prompt_scribe,
                                           model=ChatOpenAI(
                                               model_name='gpt-4o-mini',
                                               streaming=True,
                                               temperature=0.0,
                                               callbacks=[StreamingStdOutCallbackHandler()]),
                                           tools=tools)


tool_making_agent.receive("HumanUser", "can you please a create an tool that can create an bounding box around title(headers) of the image")

tool_making_agent.send()

print("Done")
