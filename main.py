import streamlit as st
import pandas as pd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Student Details Viewer",
    page_icon="📋",
    layout="wide"
)

# ---------------------------
# GOOGLE SHEET URL
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

    st.title("📋 Student Details Viewer")

    if df.empty:
        st.warning("No data found in the sheet.")
        st.stop()

    # Use first column as dropdown column
    name_column = df.columns[0]

    selected_name = st.selectbox(
        f"Select {name_column}",
        sorted(df[name_column].dropna().astype(str).unique())
    )

    result = df[df[name_column].astype(str) == selected_name]

    if not result.empty:

        row = result.iloc[0]

        st.markdown("---")
        st.subheader("Details")

        cols = st.columns(2)

        for i, column in enumerate(df.columns):
            value = row[column]

            with cols[i % 2]:
                st.info(f"**{column}**\n\n{value}")

        st.markdown("---")

        with st.expander("View Complete Record"):
            st.dataframe(result, use_container_width=True)

    else:
        st.error("Record not found.")

except Exception as e:
    st.error(f"Error loading Google Sheet: {e}")
    st.info(
        "Make sure the Google Sheet is shared as 'Anyone with the link can view'."
    )
