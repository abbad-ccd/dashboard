import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grand Bargain Visualizations", layout="wide")

st.title("YouGov Data Insights")

# GLOBAL TOGGLE
global_toggle = st.radio("Select Survey Month:", ["May", "June"], horizontal=True)

# Function to load and display HTML file with a per-chart override
def show_html_chart(title: str, may_file: str, june_file: str, height: int = 600, allow_individual_toggle: bool = False):
    st.subheader(title)

    # Use override toggle if allowed
    if allow_individual_toggle:
        month_override = st.radio(f"{title} - Month (Overrides Global)", ["Use Global", "May", "June"], horizontal=True, key=title)
        if month_override == "Use Global":
            use_june = (global_toggle == "June")
        else:
            use_june = (month_override == "June")
    else:
        use_june = (global_toggle == "June")

    filename = june_file if use_june else may_file

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html_content = f.read()
            components.html(html_content, height=height, scrolling=True)
    except FileNotFoundError:
        st.error(f"❌ Could not find {filename}")

# ---------------------------
# CHARTS
# ---------------------------
st.subheader("Demographics")
col1, col2 = st.columns(2)
with col1:
    show_html_chart("Party Affiliation", "may_party.html", "june_party.html", allow_individual_toggle=True)
with col2:
    show_html_chart("Age Distribution", "may_age_group.html", "june_age_group.html", allow_individual_toggle=True)

with st.expander("More Demographics", expanded=False):
    col3, col4 = st.columns(2)
    with col3:
        show_html_chart("Gender", "may_gender.html", "june_gender.html", allow_individual_toggle=True)
        show_html_chart("Family Income", "may_family_income.html", "june_family_income.html", allow_individual_toggle=True)
    with col4:
        show_html_chart("Race", "may_race.html", "june_race.html", allow_individual_toggle=True)
        show_html_chart("Religion", "may_religion.html", "june_religion.html", allow_individual_toggle=True)

with st.expander("The Grand Bargain vs. Current Direction", expanded=True):
    show_html_chart("The Grand Bargain vs. Current Direction Votes, Overall",
                    "may_current vs. gbp total.html", "june_current vs. gbp total.html")
    show_html_chart("For Those Who Prefer the 'Current Direction': Least Supported Proposals",
                    "may_least_supported_by_current_direction.html", "june_least_supported_by_current_direction.html")

with st.expander("Agreements and Disagreements", expanded=True):
    show_html_chart("Average Vote by Party", "may_vote_by_party.html", "june_vote_by_party.html")
    show_html_chart("Issues: Not Supported", "may_oppose_percentage_by_party.html", "june_oppose_percentage_by_party.html")
    show_html_chart("Issues: Supported", "may_support_percentage_by_party.html", "june_support_percentage_by_party.html")

with st.expander("Browse by Top Proposals", expanded=False):
    show_html_chart("Proposals: Least Supported", "may_opposed_proposals_by_party.html", "june_opposed_proposals_by_party.html")
    show_html_chart("Proposals: Most Supported", "may_supported_proposals_by_party.html", "june_supported_proposals_by_party.html")

with st.expander("By State", expanded=True):
    show_html_chart("GBP vs. Current Direction", "may_GBP vs. Current Direction.html")
    show_html_chart("Average Votes by State", "may_average_votes_by_state.html")

with st.expander("Browse by State + Issue", expanded=False):
    show_html_chart("Votes by State: Economy", "may_min_Economy.html")
    show_html_chart("Votes by State: Education", "may_min_Education.html")
    show_html_chart("Votes by State: Healthcare", "may_min_Healthcare.html")
    show_html_chart("Votes by State: Energy", "may_min_Energy.html")
    show_html_chart("Votes by State: Taxes", "may_min_Taxes.html")
    show_html_chart("Votes by State: Debt", "may_min_Debt.html")

