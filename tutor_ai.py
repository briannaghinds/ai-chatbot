"""
@author: Brianna Hinds
Description: LangGraph agent responsible for making Beginner/Intermediate/Advanced explanations of notes.
im taaking over
    - EXTRA: make quizzes for the notes
"""

# import libraries
import os  # vscode
from dotenv import load_dotenv  # vscode
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph

# define the LLM
load_dotenv()  # vscode
API = os.getenv("GOOGLE_API_KEY")  # vscode
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API,  # PUT ACTUAL API KEY
    temperature=0   # this parameter has to do with the LLM hallucinating
)

# define the AgentState
class AgentState(TypedDict):
    page_content: str
    lvl: str  # choice of the user Beginner/Intermediate/Expert
    summary: str


# define the agent
def notes_summarizer(state: AgentState) -> AgentState:
    """Summarize notes based on user-selected difficulty level"""
    prompt = f"""
    You are an AI tutor. Summarize the following notes at a {state['lvl']} level:
    
    Notes:
    {state['page_content']}
    
    Requirements:
    - Beginner: Use simple words, short sentences, everyday examples. Like you are explaining it to a little kid.
    - Intermediate: Use moderate technical terms, explain main ideas, avoid jargon.
    - Expert: Assume the reader has background knowledge, focus on depth and detail.
    """
    response = llm.invoke(prompt)
    return {"page_content": state["page_content"], "lvl": state["lvl"], "summary": response.content}


# initialize and define the graph  
workflow = StateGraph(AgentState)
workflow.add_node("summarizer", notes_summarizer)
workflow.set_entry_point("summarizer")   # start here
workflow.set_finish_point("summarizer")  # end here

# compile the agent
notes_summary = workflow.compile()