import streamlit as st
import pandas as pd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Interview Evaluation",
    page_icon="📋",
    layout="wide"
)

# ---------------------------
# GOOGLE SHEET CONFIG
# ---------------------------
SHEET_ID = "1usmOYunAIXAcuoWdsOl139LSa3p_Mloe0Hmt1QqW-pI"
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

# ---------------------------
# LOAD DATA
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL)

try:
    df = load_data()

    if df.empty:
        st.warning("No data found.")
        st.stop()

    st.title("Interview Evaluation Report")

    # Name Dropdown
    selected_name = st.selectbox(
        "Select Name",
        sorted(df["Name"].dropna().astype(str).unique()),
        index=None,
        placeholder="Select Name"
    )

    if selected_name:

        result = df[df["Name"].astype(str) == selected_name]

        if not result.empty:

            row = result.iloc[0]

            st.markdown(f"## {selected_name}")
            st.markdown("---")

            # Hide first 3 columns while displaying
            display_columns = df.columns[3:]

            cols = st.columns(2)

            for i, column in enumerate(display_columns):
                value = row[column]

                with cols[i % 2]:
                    st.info(f"**{column}**\n\n{value}")

            st.markdown("---")

            with st.expander("View Complete Record"):
                st.dataframe(
                    result[display_columns],
                    use_container_width=True
                )

except Exception as e:
    st.error(f"Error loading Google Sheet: {e}")
    st.info("Make sure the Google Sheet is shared as 'Anyone with the link can view'.")
