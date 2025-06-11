import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grand Bargain Visualizations", layout="wide")

st.title("YouGov Data Insights")

# Function to load and display an HTML file
def show_html_chart(title: str, filename: str, height: int = 600):
    st.subheader(title)
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html_content = f.read()
            components.html(html_content, height=height, scrolling=True)
    except FileNotFoundError:
        st.error(f"❌ Could not find {filename}")

st.subheader("Demographics:")

with st.expander("Demographic Overview", expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        show_html_chart("Party Affiliation", "party.html")
        show_html_chart("Age Distribution", "age_group.html")
        show_html_chart("Gender", "gender.html")

    with col2:
        show_html_chart("Family Income", "family_income.html")
        show_html_chart("Race", "race.html")
        show_html_chart("Religion", "religion.html")
        show_html_chart("Education", "education.html")

with st.expander("Agreements and Disagreements", expanded=True):
    show_html_chart("Average Vote by Party", "vote_by_party.html")
    show_html_chart("Issues: Not Supported", "oppose_percentage_by_party.html")
    show_html_chart("Issues: Supported", "support_percentage_by_party.html")
    show_html_chart("Proposals: Least Supported", "opposed_proposals_by_party.html")
    show_html_chart("Proposals: Most Supported", "supported_proposals_by_party.html")

with st.expander("Data by State", expanded=False):
    show_html_chart("GBP vs. Current Direction", "GBP vs. Current Direction.html")
    show_html_chart("Average Votes by State", "average_votes_by_state.html")

with st.expander("Browse by Issue", expanded=False):
    show_html_chart("Votes by State: Economy", "min_Economy.html")
    show_html_chart("Votes by State: Education", "min_Education.html")
    show_html_chart("Votes by State: Healthcare", "min_Healthcare.html")
    show_html_chart("Votes by State: Energy", "min_Energy.html")
    show_html_chart("Votes by State: Taxes", "min_Taxes.html")
    show_html_chart("Votes by State: Debt", "min_Debt.html")

