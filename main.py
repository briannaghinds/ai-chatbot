"""
@author: Brianna Hinds
Description: Application build and streamlit definitions
"""

import streamlit as st  # UI library
from pypdf import PdfReader  # library to read PDF content
from IPython.display import Image, display
import matplotlib.pyplot as plt

# set the page configures
st.set_page_config(
    page_title="Notes Summarizer",
    page_icon=":memo:",
    layout="wide",
)

# define a title for the page
st.title("AI Learning Tutor")
st.write("This application is an AI tutor that explains uploaded course notes in different difficulty levels (Beginner/Immediate/Advanced) and also have quizzes based on those notes")

col1, col2 = st.columns(2)
# define a place to upload a PDF document (streamlit makes this really easy)
# upload and display the file
uploaded_file = col1.file_uploader(  # NEED TO PIP INSTALL EXTENSION (pip install streamlit[pdf])
    "Upload a PDF file of your notes below.",
    accept_multiple_files=False,
    type="pdf"
)

if uploaded_file:
    # display the uploaded file
    # col2.pdf(uploaded_file)

    # extract text from all pages
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text() or ""

    # let user pick level
    lvl = col2.pills("Choose your learning level:", ["Beginner", "Intermediate", "Expert"])

    if col2.button("Summarize Notes"):
        from tutor_ai import notes_summary  # import the compiled agent
        result = notes_summary.invoke({"page_content": pdf_text, "lvl": lvl})
        col2.write(result["summary"])

        # ## GRAPH VISUALIZE ##
        # Image(notes_summary.get_graph().print_ascii())
        # plt.savefig("notes_summary.png")
        # ####