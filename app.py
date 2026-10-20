
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="College Data Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("College Data Analysis Dashboard")
st.write(
    "Explore tuition costs, graduation rates, applications, "
    "and enrollment across colleges."
)

@st.cache_data
def load_college_data():
    return pd.read_csv("College.csv")

College = load_college_data()

college_type = st.sidebar.selectbox(
    "Select College Type",
    ["All Colleges", "Private Colleges", "Public Colleges"]
)

if college_type == "Private Colleges":
    filtered_data = College[College["Private"] == "Yes"]
elif college_type == "Public Colleges":
    filtered_data = College[College["Private"] == "No"]
else:
    filtered_data = College.copy()

st.subheader("Dashboard Overview")
st.write(f"Number of colleges displayed: {len(filtered_data)}")

col1, col2 = st.columns(2)

with col1:
    fig1 = px.histogram(
        filtered_data,
        x="Outstate",
        nbins=25,
        title="Distribution of Out-of-State Tuition",
        labels={"Outstate": "Tuition (USD per year)"}
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.histogram(
        filtered_data,
        x="Grad.Rate",
        nbins=25,
        title="Distribution of Graduation Rates",
        labels={"Grad.Rate": "Graduation Rate (%)"}
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    fig3 = px.scatter(
        filtered_data,
        x="Apps",
        y="Enroll",
        hover_data=["Private", "Outstate", "Grad.Rate"],
        title="Applications vs. Enrollment",
        labels={
            "Apps": "Number of Applications",
            "Enroll": "Number of Enrolled Students"
        }
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    fig4 = px.scatter(
        filtered_data,
        x="Outstate",
        y="Grad.Rate",
        size="Apps",
        color="Private",
        hover_data=["Apps", "Enroll"],
        title="Tuition, Graduation Rate, and Applications",
        labels={
            "Outstate": "Tuition (USD per year)",
            "Grad.Rate": "Graduation Rate (%)",
            "Private": "Private College"
        },
        size_max=35
    )
    st.plotly_chart(fig4, use_container_width=True)

st.subheader("Filtered Data Preview")
st.dataframe(filtered_data.head(10), use_container_width=True)
