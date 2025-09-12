
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Student Mental Health Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------- SIDEBAR FILTERS ---------------- #
st.sidebar.header("🎓 Student Mental Health Filters")
semester = st.sidebar.selectbox("Select Semester", ["Spring", "Fall"])
study_hours = st.sidebar.slider("Average Study Hours/Day", 0, 12, 6)
stress_level = st.sidebar.radio("Self-Reported Stress Level", ["Low", "Medium", "High"])

# ---------------- SYNTHETIC DATA ---------------- #
np.random.seed(42)
students = [f"Student {i}" for i in range(1, 21)]
cgpa = np.random.uniform(2.5, 4.0, size=20)          # Academic performance
stress_scores = np.random.randint(1, 100, size=20)   # Stress levels
sleep_hours = np.random.uniform(4, 9, size=20)       # Average sleep

df = pd.DataFrame({
    "Student": students,
    "CGPA": cgpa.round(2),
    "Stress Score": stress_scores,
    "Sleep Hours": sleep_hours.round(1)
})

# ---------------- MAIN LAYOUT ---------------- #
st.title("📊 Student Mental Health Dashboard")
st.write("This dashboard uses **synthetic data** to demonstrate basic analytics for student wellness.")

# Data preview
st.subheader("Student Data Preview")
st.dataframe(df.head())

# ---------------- CHARTS -----------

# ---------------- CHARTS ---------------- #
st.subheader("Stress Score Distribution")
fig1 = px.bar(df, x="Student", y="Stress Score", title="Stress Scores by Student", color="Stress Score")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Sleep Hours vs CGPA")
fig2 = px.scatter(
    df, x="Sleep Hours", y="CGPA",
    size="Stress Score", color="Stress Score",
    hover_name="Student", title="Relationship Between Sleep Hours and CGPA"
)
st.plotly_chart(fig2, use_container_width=True)





