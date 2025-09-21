**explain streamlit basics and langgraph basics (initialization, agent state, building)**
# Introduction to `LangGraph` and `streamlit`

## What is `LangGraph`
LangGraph is an open-source framework that allows control of agent workflows. There are other "Lang-family" libraries that allow for agentic agent building. There is also Langchain. LangGraph is uses concepts and structures from graph theory to build complex AI workflows. LangChain on the other hand is used for simple, linear workflows.

> Question. So *why* LangGraph?

### Reason 1: I am more comfortable with it...
### Reason 2: LangGraph is very low-level compared to LangChain. But that doesn't mean one is better than the other, they each have different use cases.
### Reason 3: LangGraph is built for production grade, complex, multi-agent systems.

Below is an example of one of my MAS graphs.

![Financial Fraud MAS Graph](https://github.com/briannaghinds/ai-chatbot/blob/main/Introduction/fraud_detector_graph.png)

### LangGraph basics
```python
# basic imports
from typing import TypedDict  # this is used for the agent state (holds the memory)


# define the AgentState
class AgentState(TypedDict):
    some_variable: type  # you will define some variable and its data type
    some_variable1: type

# define the nodes/agents
def agent1(state: AgentState) -> AgentState

# define the graph + nodes

# build the graph

# call the graph workflow
```

## What is `streamlit`?
Docs: https://docs.streamlit.io/develop/api-reference

