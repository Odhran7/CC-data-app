# Facilitate Messaging
import streamlit as st
from data import util
from datetime import datetime

st.title("Create a new message")

table_name = "message"

conn = util.get_connection()
userHostID = st.text_input("User Host ID")
userTenantID = st.text_input("User Tenant ID")
text = st.text_input("Create text message")
date_submitted = st.text_input("Value for date (default is today)", value=datetime.today().strftime('%Y-%m-%d:%H:%M:%S'))

list_of_values = [
    userHostID,
    userTenantID,
    text,
    date_submitted
]
# We use a form to control when the page is (re)loaded and hence when the row is attempted to be added.
with st.form("form"):
    submitted = st.form_submit_button("Add new message")

if submitted:
    conn._instance.execute(
        f"insert into {table_name} values (?, ?, ?, ?)", # if you add more input values, add a question mark for each one
        list_of_values,
    )
    row_count = conn.query(
        f"select count(1) from {table_name}",
        ttl=0, # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"{table_name} now has {row_count.iat[0,0]} rows.")
