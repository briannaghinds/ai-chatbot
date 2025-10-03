# AI Notes Summarizer 📚

In this project, we'll build an **AI Notes Summarizer** to help you study. It uses a **Google Gemini LLM** (via the LangChain library) to process notes and the **Streamlit** Python library to build a simple, interactive user interface.

The application acts as an AI tutor, explaining uploaded course notes at different difficulty levels you choose: **Beginner**, **Intermediate**, or **Expert**.

---

## Application Setup Steps:

This guide assumes you are working within a local environment using a text editor like VS Code or PyCharm, and a Python environment (e.g., Anaconda or a virtual environment).

### Step 1: Create the Project Environment

1.  **Define a Project Folder:** Create a new, empty folder on your system (e.g., `ai-notes-summarizer`).
2.  **Open in Editor:** Open this folder in your chosen text editor (like VS Code or PyCharm).
3.  **Install Libraries:** Open your terminal/command prompt and run the following commands to install the necessary Python libraries:

    ```bash
    pip install streamlit pypdf python-dotenv langchain_google_genai langgraph
    ```

    * `streamlit`: For building the user interface.
    * `pypdf`: For reading and extracting text from PDF files.
    * `python-dotenv`: To securely load your API key from a local file.
    * `langchain_google_genai`: The specific LangChain package for interacting with Google Gemini models.
    * `langgraph`: For defining the simple flow (or "graph") of the AI agent.

---

### Step 2: Get Your API Key and Set Up the Environment File

1.  **Get API Key:** Go to **Google AI Studio** (`ai.studio.google.com`) and navigate to the **API keys** section on the left-hand menu. Generate a new API key and **copy it**.
2.  **Create `.env` File:** In the root of your project folder, create a new file named **`.env`** (ensure it has no file extension).
3.  **Add Key to `.env`:** Inside the `.env` file, paste your API key in the following format:

    ```bash
    GOOGLE_API_KEY="YOUR_COPIED_API_KEY_VALUE_HERE"
    ```
    Replace `"YOUR_COPIED_API_KEY_VALUE_HERE"` with the key you copied from Google AI Studio.

---

### Step 3: Create the Python Files

Create two new Python files in the root of your project folder:

1.  `main.py`: This file will contain all the **Streamlit (UI) logic**.
2.  `tutor_ai.py`: This file will house the **LangGraph and Gemini LLM logic**.

---

### Step 4: Write the Code

Follow along to write the code for `tutor_ai.py` and `main.py` using the provided, commented examples below.

---

### Step 5: Run the Application

Once both files are complete, open your terminal in the project folder and run the Streamlit application with the following command:

```bash
streamlit run main.py
```
or if `streamlit` is not a recognizable command try:
```bash
python -m streamlit run main.py
```
Then a browser window will automatically open, showing your AI Notes Summarizer!

If you have any question contact Brianna Hinds (hindsbg@hc.edu)