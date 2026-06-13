import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Interview Evaluation Report",
    page_icon="📋",
    layout="wide"
)

# Sheet1 URL
CSV_URL = "https://docs.google.com/spreadsheets/d/1usmOYunAIXAcuoWdsOl139LSa3p_Mloe0Hmt1QqW-pI/export?format=csv&gid=2049735784"

@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL)

try:
    df = load_data()

    st.title("Interview Evaluation Report")

    selected_name = st.selectbox(
        "Select Name",
        sorted(df["Name"].dropna().astype(str).unique()),
        index=None,
        placeholder="Select Name"
    )

    if selected_name:

        row = df[df["Name"].astype(str) == selected_name].iloc[0]

        st.markdown(f"## {selected_name}")

        info1, info2, info3 = st.columns(3)

        with info1:
            st.info(f"**Class**\n\n{row['Class']}")

        with info2:
            st.info(f"**Course**\n\n{row['Course']}")

        with info3:
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
