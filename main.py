"""
@author: Brianna Hinds
Description: Application build and streamlit definitions
"""

import streamlit as st  # UI library
from pypdf import PdfReader  # library to read PDF content

# define a title for the page
st.title("AI Learning Tutor")
st.write("This application is an AI tutor that explains uploaded course notes in different difficulty levels (Beginner/Immediate/Advanced) and also have quizzes based on those notes")

# define a place to upload a PDF document (streamlit makes this really easy)
# upload and display the file
uploaded_file = st.file_uploader(  # NEED TO PIP INSTALL EXTENSION (pip install streamlit[pdf])
    "Upload a PDF file of your notes below.",
    accept_multiple_files=False,
    type="pdf"
)

if uploaded_file:
    st.pdf(uploaded_file)

    # extract text from all pages
    reader = PdfReader(uploaded_file)
    pdf_text = ""
    for page in reader.pages:
        pdf_text += page.extract_text() or ""

    # let user pick level
    lvl = st.pills("Choose your learning level:", ["Beginner", "Intermediate", "Expert"])

    if st.button("Summarize Notes"):
        from tutor_ai import notes_summary  # import the compiled agent
        result = notes_summary.invoke({"page_content": pdf_text, "lvl": lvl})
        st.write(result["summary"])
