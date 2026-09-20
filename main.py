import sqlite3
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

db = SQLDatabase.from_uri("sqlite:///Database/shop.db") # URI format for sqlite

print("connected databse",db.get_usable_table_names()) # check to ensure lanchain sees the table

llm = ChatOllama(model = "qwen2.5:7b", temperature=0)
toolkit = SQLDatabaseToolkit(db=db,llm = llm)

tools = toolkit.get_tools()

agent = create_agent(
    model = llm,
    tools = tools
)

#print(response["messages"][-1].content)

prompt = ChatPromptTemplate.from_messages(
  [
  ("system","You are a helpful assitant that answers the user according to the sql database"),
  ("user","Question:{question}")
  ]
)

st.title("SQL Agent")
input_text = st.text_input("ask the question")

output_parser = StrOutputParser()

response = agent.invoke({
    "messages": [
        {
           "role": "user",
            "content": input_text
        }
    ] 
})

if input_text:
    st.write(response["messages"][-1].content)