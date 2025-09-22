# AI Notes Summarizer
In this project we will build an AI Notes Summarizer to help you study via a LLM API and we will build the UI using the `streamlit` Python library.

The learning tutor, will explain uploaded course notes in different difficult levels of your choosing (Beginner/Intermediate/Advanced) and if we have time, the application will give a quiz based on those notes.

## Application Setup Steps:
### Step 1:
Define a project folder somewhere on your system. Open vscode and open that project folder (it can be empty for now).

### Step 2: 
Define a GitHub repo, start on github.com and create a new public repository. 

Go to the project folder in vscode and run

```bash
git init  # initialize this project folder
git add .  # adds everything
git commit -m "Initial commit"   # saves changes as a new commit with a description
git remote add origin https://github.com/your-username/your-repo-name.git  # connect the remote repository
git push -u origin main  # pushes all changes to the main branch
```
You now have the project set up and from this point forward the only commands you will use is
```bash
git add .
git commit -m "COMMIT MESSAGE"
git push
```

### Step 3: 
Add two Python files labeled `main.py` (this will house the `streamlit` logic) and `tutor_ai.py` (this will house the LangGraph and LLM logic)

### Step 4: 
Define a `.gitignore` and `.env` file to house the API key. This will allow you to push everything onto GitHub without exposing your API key.

```bash
# Create the file at the root of the project
Set-Content -Path .gitignore -Value ".env"  # puts .env in 

# Create a .env file
New-Item -Path . -Name ".env" -ItemType "File"

# then you can just write and load the file
```

### Step 5: 
Go to ai.studio.google.com