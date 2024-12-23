import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for storing time log data
if 'time_log' not in st.session_state:
    st.session_state['time_log'] = []

# App Title
st.title("Software Development Time Tracker")

# Activity Categories
categories = [
    "Gathering Ideas/Requirements",
    "Understanding Domain Information",
    "Running Code",
    "Testing Code",
    "End-to-End Testing",
    "Unit Testing",
    "Regression Testing",
    "Calibrating AI Models",
    "Guiding AI Models"
]

# Input Form for Logging Time
with st.form("time_entry_form"):
    st.subheader("Log Your Activity")
    activity = st.selectbox("Select Activity", categories)
    description = st.text_input("Description (Optional)")
    time_spent = st.number_input("Time Spent (in minutes)", min_value=1, step=1)
    submit_time = st.form_submit_button("Add Entry")

    if submit_time:
        st.session_state['time_log'].append({
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Activity": activity,
            "Description": description,
            "Time Spent (Minutes)": time_spent
        })
        st.success("Time entry added successfully!")

# Display Logged Activities
if st.session_state['time_log']:
    st.subheader("Logged Activities")
    df = pd.DataFrame(st.session_state['time_log'])
    st.dataframe(df)

    # Download CSV
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="time_log.csv",
        mime="text/csv"
    )
else:
    st.info("No activities logged yet. Use the form above to log your time.")
