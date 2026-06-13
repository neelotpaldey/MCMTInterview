import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interview Evaluation", layout="wide")

# Google Sheet CSV URL
sheet_url = "https://docs.google.com/spreadsheets/d/1usmOYunAIXAcuoWdsOl139LSa3p_Mloe0Hmt1QqW-pI/export?format=csv"

@st.cache_data
def load_data():
    return pd.read_csv(sheet_url)

df = load_data()

st.title("Interview Evaluation Report")

# Name dropdown
selected_name = st.selectbox(
    "Select Student",
    sorted(df["Name"].dropna().unique())
)

# Selected row
student = df[df["Name"] == selected_name]

if not student.empty:
    row = student.iloc[0]

    st.subheader(f"Report Card: {selected_name}")

    for col in df.columns:
        st.metric(col, row[col])

    st.dataframe(student, use_container_width=True)
