from langchain import hub
prompt = hub.pull("hwchase17/react")
print(prompt)

from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_community.chat_models.tongyi import ChatTongyi
llm = ChatTongyi(
    model_name="qwen-plus"
)

from langchain_community.utilities import SerpAPIWrapper
from langchain.agents.tools import Tool

search = SerpAPIWrapper()

tools = [
    Tool(
        name="Search",
        func=search.run,
        description="当模型没有相关知识时，用于搜索知识"
    ),
]

from langchain.agents import create_react_agent
agent = create_react_agent(llm, tools, prompt)
from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=True)
agent_executor.invoke({"input":"当前Agent最新研究进展是什么？"})