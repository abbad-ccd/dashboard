import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grand Bargain Visualizations", layout="wide")

st.title("📊 Grand Bargain Project: Interactive Visualizations")
st.markdown("Explore key insights from participants across different states and questions.")

# Function to load and display an HTML file
def show_html_chart(title: str, filename: str, height: int = 600):
    st.subheader(title)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html_content = f.read()
            components.html(html_content, height=height, scrolling=True)
    except FileNotFoundError:
        st.error(f"❌ Could not find {filename}")

# Display all three charts
show_html_chart("🧭 GBP vs. Current Direction", "GBP vs. Current Direction.html")
show_html_chart("📊 Average Votes by State", "average_votes_by_state.html")
show_html_chart("🗺️ Participants by State", "participants_by_state.html")
