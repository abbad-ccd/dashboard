import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grand Bargain Visualizations", layout="wide")

st.title("YouGov Data Insights")

# GLOBAL TOGGLE
global_toggle = st.radio("Select Global Survey Month:", ["May", "June"], horizontal=True)

# Section-specific toggle
def section_toggle(section_title: str):
    return st.radio(f"{section_title} – Select Month", ["Global", "May", "June"], horizontal=True, key=f"toggle_{section_title}")

# Chart display function
def show_html_chart(title: str, may_file: str, june_file: str = None, height: int = 600, month_override: str = "Global"):
    st.subheader(title)

    if month_override == "Global":
        use_june = (global_toggle == "June")
    else:
        use_june = (month_override == "June")

    filename = june_file if use_june and june_file else may_file

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html_content = f.read()
            components.html(html_content, height=height, scrolling=True)
    except FileNotFoundError:
        st.error(f"❌ Could not find {filename}")

# ---------------------------
# CHARTS
# ---------------------------

# DEMOGRAPHICS
st.subheader("Demographics")
demographics_month = section_toggle("Demographics")
col1, col2 = st.columns(2)
with col1:
    show_html_chart("Party Affiliation", "may_party.html", "june_party.html", month_override=demographics_month)
with col2:
    show_html_chart("Age Distribution", "may_age_group.html", "june_age_group.html", month_override=demographics_month)

with st.expander("More Demographics", expanded=False):
    more_demo_month = section_toggle("More Demographics")
    col3, col4 = st.columns(2)
    with col3:
        show_html_chart("Gender", "may_gender.html", "june_gender.html", month_override=more_demo_month)
        show_html_chart("Family Income", "may_family_income.html", "june_family_income.html", month_override=more_demo_month)
    with col4:
        show_html_chart("Race", "may_race.html", "june_race.html", month_override=more_demo_month)
        show_html_chart("Religion", "may_religion.html", "june_religion.html", month_override=more_demo_month)

# GRAND BARGAIN VS CURRENT DIRECTION
with st.expander("The Grand Bargain vs. Current Direction", expanded=True):
    gbp_month = section_toggle("Grand Bargain Section")
    show_html_chart("The Grand Bargain vs. Current Direction Votes, Overall",
                    "may_current vs. gbp total.html", "june_current vs. gbp total.html", month_override=gbp_month)
    show_html_chart("For Those Who Prefer the 'Current Direction': Least Supported Proposals",
                    "may_least_supported_by_current_direction.html", "june_least_supported_by_current_direction.html", month_override=gbp_month)

# AGREEMENTS AND DISAGREEMENTS
with st.expander("Agreements and Disagreements", expanded=True):
    agree_month = section_toggle("Agreements and Disagreements")
    show_html_chart("Average Vote by Party", "may_vote_by_party.html", "june_vote_by_party.html", month_override=agree_month)
    show_html_chart("Issues: Not Supported", "may_oppose_percentage_by_party.html", "june_oppose_percentage_by_party.html", month_override=agree_month)
    show_html_chart("Issues: Supported", "may_support_percentage_by_party.html", "june_support_percentage_by_party.html", month_override=agree_month)

# TOP PROPOSALS
with st.expander("Browse by Top Proposals", expanded=False):
    proposals_month = section_toggle("Browse by Top Proposals")
    show_html_chart("Proposals: Least Supported", "may_opposed_proposals_by_party.html", "june_opposed_proposals_by_party.html", month_override=proposals_month)
    show_html_chart("Proposals: Most Supported", "may_supported_proposals_by_party.html", "june_supported_proposals_by_party.html", month_override=proposals_month)

# BY STATE
with st.expander("By State", expanded=True):
    state_month = section_toggle("By State")
    show_html_chart("GBP vs. Current Direction", "may_GBP vs. Current Direction.html", "june_GBP_vs_Current_Direction.html", month_override=state_month)
    show_html_chart("Average Votes by State", "may_average_votes_by_state.html", "june_proposal_support_by_state.html", month_override=state_month)

# BY STATE + ISSUE
with st.expander("Browse by State + Issue", expanded=False):
    state_issue_month = section_toggle("Browse by State + Issue")
    show_html_chart("Votes by State: Economy", "may_min_Economy.html", month_override=state_issue_month)
    show_html_chart("Votes by State: Education", "may_min_Education.html", month_override=state_issue_month)
    show_html_chart("Votes by State: Healthcare", "may_min_Healthcare.html", month_override=state_issue_month)
    show_html_chart("Votes by State: Energy", "may_min_Energy.html", month_override=state_issue_month)
    show_html_chart("Votes by State: Taxes", "may_min_Taxes.html", month_override=state_issue_month)
    show_html_chart("Votes by State: Debt", "may_min_Debt.html", month_override=state_issue_month)
