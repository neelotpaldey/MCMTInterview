import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Interview Evaluation Report",
    page_icon="📋",
    layout="wide"
)

CSV_URL = "https://docs.google.com/spreadsheets/d/1usmOYunAIXAcuoWdsOl139LSa3p_Mloe0Hmt1QqW-pI/export?format=csv"

@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL)

try:
    df = load_data()

    # Clean column names
    df.columns = df.columns.astype(str).str.strip()

    st.title("Interview Evaluation Report")

    # Use first column as Name column
    name_col = df.columns[0]

    selected_name = st.selectbox(
        "Select Name",
        sorted(df[name_col].dropna().astype(str).unique()),
        index=None,
        placeholder="Select Name"
    )

    if selected_name:

        row = df[df[name_col].astype(str) == selected_name].iloc[0]

        st.markdown(f"## {selected_name}")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.info(f"**Class**\n\n{row[df.columns[1]]}")

        with c2:
            st.info(f"**Course**\n\n{row[df.columns[2]]}")

        with c3:
            st.info(f"**University**\n\n{row[df.columns[3]]}")

        st.markdown("---")
        st.subheader("Evaluation Scores")

        score_columns = df.columns[4:]

        cols = st.columns(2)

        for i, col in enumerate(score_columns):
            with cols[i % 2]:
                st.info(f"**{col}**\n\n{row[col]}")

except Exception as e:
    st.error(f"Error loading data: {e}")
