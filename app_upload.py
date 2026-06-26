"""
Web-based knowledge base upload service built with Streamlit.

Streamlit re-executes the script whenever a page element changes,
so state should be maintained through session_state.
"""
import time
import streamlit as st

from knowledge_base import KnowledgeBaseService


# Page title
st.title("Knowledge Base Update Service")

# File uploader
uploaded_file = st.file_uploader(
    "Please upload a TXT file",
    type=["txt"],
    accept_multiple_files=False,  # Only one file can be uploaded
)

# Store service instance in session state
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploaded_file is not None:
    # Extract file information
    file_name = uploaded_file.name
    file_type = uploaded_file.type
    file_size_kb = uploaded_file.size / 1024

    st.subheader(f"File Name: {file_name}")
    st.write(f"Type: {file_type} | Size: {file_size_kb:.2f} KB")

    # Convert uploaded file bytes to UTF-8 text
    text_content = uploaded_file.getvalue().decode("utf-8")

    # Display a loading spinner while updating the knowledge base
    with st.spinner("Loading knowledge base..."):
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(
            text_content,
            file_name
        )
        st.write(result)
