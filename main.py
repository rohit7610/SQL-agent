import sqlite3
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

db = SQLDatabase.from_uri("sqlite:///Database/shop.db") # URI format for sqlite

print("connected databse",db.get_usable_table_names()) # check to ensure lanchain sees the table

llm = ChatOllama(model = "qwen2.5:7b", temperature=0)
toolkit = SQLDatabaseToolkit(db=db,llm = llm)

tools = toolkit.get_tools()

agent = create_agent(
    model = llm,
    tools = tools
)

question = input("Ask a question")

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ] 
})

print(response["messages"][-1].content)