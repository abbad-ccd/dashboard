import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title="Grand Bargain Visualizations", layout="wide")

st.title("YouGov Data Insights")

# Section-specific toggle (May, June, July)
def section_toggle(section_title: str):
    return st.radio(f"{section_title} – Select Month", ["May", "June", "July"], horizontal=True, key=f"toggle_{section_title}")

# Chart display function using section month
def show_html_chart(title: str, may_file: str, june_file: str = None, july_file: str = None, height: int = 600, month: str = "May"):
    st.subheader(title)

    filename = may_file
    if month == "June" and june_file:
        filename = june_file
    elif month == "July" and july_file:
        filename = july_file

    try:
        if filename.endswith(".html"):
            with open(filename, 'r', encoding='utf-8') as f:
                html_content = f.read()
                components.html(html_content, height=height, scrolling=True)
        elif filename.endswith(".png") or filename.endswith(".jpg"):
            st.image(filename, use_container_width=True)
        else:
            st.warning(f"⚠️ Unsupported file type: {filename}")
    except FileNotFoundError:
        st.error(f"❌ Could not find {filename}")

# ---------------------------
# CHARTS
# ---------------------------

with st.expander("The Grand Bargain vs. Current Direction", expanded=True):
    gbp_month = section_toggle("Grand Bargain Section")
    show_html_chart("The Grand Bargain vs. Current Direction Votes, Overall",
                    "may_current vs. gbp total.html", 
                    "june_current vs. gbp total.html",
                    "july_current vs. gbp total.html",
                    month=gbp_month)

with st.expander("Those who prefer the \"Current Direction\": Demographic bias", expanded=True):
    show_html_chart("Party affiliation of those preferring the current direction", "rejectors_by_party_june_vs_july.html")

with st.expander("Changes in the data from June to July", expanded=True):
    # Toggle to select comparison period
    period = st.radio(
        "Select comparison period:",
        options=["May → June", "June → July"],
        index=1,  # Default to "June → July"
        horizontal=True,
        key="change_period_toggle"
    )

    if period == "May → June":
        show_html_chart(
            "Change by issue: Circles show the starting point in May, arrows show the direction of the change in June",
            "issue_change_in_opposition_may_to_june.html",
            "issue_change_in_opposition_may_to_june.html"
        )

        show_html_chart(
            "Change by proposal: Circles show the starting point in May, arrows show the direction of the change in June",
            "proposal_change_in_opposition_may_to_june_all.html",
            "proposal_change_in_opposition_may_to_june_all.html"
        )
    else:  # "June → July"
        show_html_chart(
            "Change by issue: Circles show the starting point in June, arrows show the direction of the change in July",
            "issue_change_in_opposition_may_to_june.html",   # fallback May-Jun as baseline file? You can replace this if July-specific base is available
            "issue_change_in_opposition_june_to_july.html"
        )

        show_html_chart(
            "Change by proposal: Circles show the starting point in June, arrows show the direction of the change in July",
            "proposal_change_in_opposition_may_to_june_all.html",  # fallback May-Jun baseline file
            "proposal_change_in_opposition_june_to_july_all.html"
        )

with st.expander("Those who prefer the \"Current Direction\": Demographic bias", expanded=False):
    show_html_chart("Demographic biases: Blue represents the respondent average, red represent the trends among those preferring the current direction",
                    "GBP_reject_demographic_bias_all.html")

with st.expander("Who can we persuade?", expanded=True):
    show_html_chart("The top reasons we have seen people mention when they choose the \"Current Direction\" instead of the Grand Bargain",
                    "Top topics.png")

with st.expander("Agreements and Disagreements", expanded=True):
    agree_month = section_toggle("Agreements and Disagreements")
    show_html_chart("Issues: Not Supported",
                    "may_oppose_percentage_by_party.html",
                    "june_oppose_percentage_by_party.html",
                    "july_oppose_percentage_by_party.html",
                    month=agree_month)
    show_html_chart("Issues: Supported",
                    "may_support_percentage_by_party.html",
                    "june_support_percentage_by_party.html",
                    "july_support_percentage_by_party.html",
                    month=agree_month)

with st.expander("Browse by Top Proposals", expanded=False):
    proposals_month = section_toggle("Browse by Top Proposals")
    show_html_chart("Proposals: Least Supported",
                    "may_opposed_proposals_by_party.html",
                    "june_opposed_proposals_by_party.html",
                    "july_opposed_proposals_by_party.html",
                    month=proposals_month)
    show_html_chart("Proposals: Most Supported",
                    "may_supported_proposals_by_party.html",
                    "june_supported_proposals_by_party.html",
                    "july_supported_proposals_by_party.html",
                    month=proposals_month)

with st.expander("By State", expanded=True):
    state_month = section_toggle("By State")
    show_html_chart("GBP vs. Current Direction",
                    "may_GBP vs. Current Direction.html",
                    "june_GBP_vs_Current_Direction.html",
                    "july_GBP_vs_Current_Direction.html",
                    month=state_month)
    show_html_chart("Average Votes by State",
                    "may_average_votes_by_state.html",
                    "june_proposal_support_by_state.html",
                    "july__proposal_support_by_state.html",
                    month=state_month)

st.subheader("Demographics")
demographics_month = section_toggle("Demographics")
col1, col2 = st.columns(2)
with col1:
    show_html_chart("Party Affiliation",
                    "may_party.html",
                    "june_party.html",
                    "july_party.html",
                    month=demographics_month)
with col2:
    show_html_chart("Age Distribution",
                    "may_age_group.html",
                    "june_age_group.html",
                    "july_age_group.html",
                    month=demographics_month)

with st.expander("More Demographics", expanded=False):
    more_demo_month = section_toggle("More Demographics")
    col3, col4 = st.columns(2)
    with col3:
        show_html_chart("Gender",
                        "may_gender.html",
                        "june_gender.html",
                        "july_gender.html",
                        month=more_demo_month)
        show_html_chart("Family Income",
                        "may_family_income.html",
                        "june_family_income.html",
                        "july_family_income.html",
                        month=more_demo_month)
    with col4:
        show_html_chart("Race",
                        "may_race.html",
                        "june_race.html",
                        "july_race.html",
                        month=more_demo_month)
        show_html_chart("Religion",
                        "may_religion.html",
                        "june_religion.html",
                        "july_religion.html",
                        month=more_demo_month)
