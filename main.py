"""
@author: Brianna Hinds
Description: Application build and streamlit definitions
"""
# import libraries
import streamlit as st  # UI library
from pypdf import PdfReader  # library to read PDF content

# --- Configure and Define the Application UI Elements --- #
st.set_page_config(
    page_title="Notes Summarizer",
    page_icon=":memo:",
    layout="wide",
)

# define a title for the page and introductory text
st.title("AI Learning Tutor")
st.write("This application is an AI tutor that explains uploaded course notes in different difficulty levels (Beginner/Immediate/Advanced).")

# define streamlit columns so our elements can have a clean layout
col1, col2 = st.columns()

# define a place to upload a PDF document in the first column (streamlit makes this really easy)
uploaded_file = col1.file_uploader(  # NEED TO PIP INSTALL EXTENSION (pip install streamlit[pdf])
    "Upload a PDF file of your notes below.",
    accept_multiple_files=False,
    type="pdf"  # restrict the files to be uploaded by the user to ONLY pdf
)


# --- Conditional Logic: this runs ONLY IF there is a file uploaded by the user --- #
if uploaded_file:
    # STEP 1: extract text from pdf pages
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        # extract the text from each page and append to the pdf_text string
        pdf_text += page.extract_text() or ""

    # STEP 2: let user pick a difficultly level
    lvl = col2.radio("Choose your learning level:", ["Beginner", "Intermediate", "Expert"])

    # STEP 3: define a button for the user to press when they want the LLM to summarize
    if col2.button("Summarize Notes"):
        from tutor_ai import notes_summary  # import the compiled agent from your ai file, you import from the name of your file that has the AI logic
        
        # invoke the compiled agent with all the collected data (page content and level)
        # this line will send the data to the notes_summarizer function defined in the tutor_ai.py file
        result = notes_summary.invoke({"page_content": pdf_text, "lvl": lvl})

        # display the final summary content on the steamlit application
        col2.write(result["summary"])