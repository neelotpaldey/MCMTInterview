import streamlit as st
import pandas as pd

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="Interview Evaluation Report",
    page_icon="📋",
    layout="wide"
)

# ----------------------------
# GOOGLE SHEET SETTINGS
# ----------------------------
SHEET_ID = "1usmOYunAIXAcuoWdsOl139LSa3p_Mloe0Hmt1QqW-pI"

# Replace with Sheet1 gid if different
SHEET1_GID = "0"

CSV_URL = (
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export"
    f"?format=csv&gid={SHEET1_GID}"
)

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(CSV_URL)
    df.columns = df.columns.astype(str).str.strip()
    return df

try:
    df = load_data()

    st.title("📋 Interview Evaluation Report")

    if df.empty:
        st.warning("No data found.")
        st.stop()

    # Name dropdown
    selected_name = st.selectbox(
        "Select Name",
        sorted(df["Name"].dropna().astype(str).unique()),
        index=None,
        placeholder="Select Name"
    )

    if selected_name:

        row = df[df["Name"].astype(str) == selected_name].iloc[0]

        st.markdown(f"## 👤 {selected_name}")

        # Student Info
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info(f"**Class**\n\n{row['Class']}")

        with col2:
            st.info(f"**Course**\n\n{row['Course']}")

        with col3:
            st.info(f"**University**\n\n{row['University']}")

        st.markdown("---")
        st.subheader("Evaluation Scores")

        # Skip Name, Class, Course, University
        score_columns = df.columns[4:]

        cols = st.columns(2)

        for i, col in enumerate(score_columns):
            with cols[i % 2]:
                st.info(f"**{col}**\n\n{row[col]}")

except Exception as e:
    st.error(f"Error loading data: {e}")

    st.info(
        "If the error persists, verify that:\n"
        "1. Sheet1 is shared as 'Anyone with the link can view'.\n"
        "2. SHEET1_GID matches the gid of Sheet1."
    )
