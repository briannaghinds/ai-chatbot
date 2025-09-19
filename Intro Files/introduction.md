explain streamlit basics and langgraph basics (initialization, agent state, building)
# Introduction to `LangGraph` and `streamlit`

## What is `LangGraph`
LangGraph is an open-source framework that allows control of agent workflows. There are other "Lang-family" libraries that allow for agentic agent building. There is also Langchain. LangGraph is uses concepts and structures from graph theory to build complex AI workflows. LangChain on the other hand is used for simple, linear workflows.

> Question. So *why* LangGraph?

### Reason 1: I am more comfortable with it.
### Reason 2: LangGraph is very low-level compared to LangChain.
### Reason 3: LangGraph is built for production grade, complex, multi-agent systems.

Below is an example of one of my MAS graphs.

![Financial Fraud MAS Graph](https://github.com/briannaghinds/ai-chatbot/blob/main/Intro%20Files/fraud_detector_graph.png)