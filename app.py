import streamlit as st

# Set page title
st.set_page_config(page_title="Participants by State")

st.title("Participants by State - Interactive Map")

# Load and display the HTML file
with open("participants_by_state.html", 'r', encoding='utf-8') as f:
    html_content = f.read()

# Display the HTML inside an iframe
st.components.v1.html(html_content, height=600, scrolling=True)
