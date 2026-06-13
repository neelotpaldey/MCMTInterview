import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Interview Evaluation Report",
    page_icon="📋",
    layout="wide"
)

CSV_URL = "https://docs.google.com/spreadsheets/d/1usmOYunAIXAcuoWdsOl139LSa3p_Mloe0Hmt1QqW-pI/gviz/tq?tqx=out:csv&sheet=Sheet1"

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_URL)
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()

    st.title("📋 Interview Evaluation Report")

    selected_name = st.selectbox(
        "Select Name",
        sorted(df["Name"].dropna().unique()),
        index=None,
        placeholder="Select Name"
    )

    if selected_name:

        row = df[df["Name"] == selected_name].iloc[0]

        st.markdown(f"## 👤 {selected_name}")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.info(f"**Class**\n\n{row['Class']}")

        with c2:
            st.info(f"**Course**\n\n{row['Course']}")

        with c3:
            st.info(f"**University**\n\n{row['University']}")

        st.markdown("---")
        st.subheader("Evaluation Scores")

        score_columns = df.columns[4:]

        cols = st.columns(2)

        for i, col in enumerate(score_columns):
            with cols[i % 2]:
                st.info(f"**{col}**\n\n{row[col]}")

except Exception as e:
    st.error(f"Error loading data: {e}")
