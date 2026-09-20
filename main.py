import sqlite3
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

db = SQLDatabase.from_uri("sqlite:///Database/shop.db") # URI format for sqlite

print("connected databse",db.get_usable_table_names()) # check to ensure lanchain sees the table

llm = ChatOllama(model = "qwen2.5:7b", temperature=0)
toolkit = SQLDatabaseToolkit(db=db,llm = llm)

agent = create_sql_agent(
    llm = llm,
    toolkit=toolkit,
    verbose=True,
    handle_parsing_errors=True
)

question = input("Ask a question")

response = agent.invoke({"input": question})

print(response["output"])