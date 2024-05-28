# This is request human support tickets

import streamlit as st
from data import util
from datetime import datetime

st.title("Add a ticket for support")
st.warning("If you see errors, ensure you've created the table(s) first using the `Seed Data` pages.")

table_name = "support"

conn = util.get_connection()

client_id = st.text_input("Value for client ID")
rental_date = st.text_input("Value for rental date (default is today)", value=datetime.today().strftime('%Y-%m-%d'))
equipment_needed = st.text_input("Value for equipment needed")
rental_duration = st.text_input("Value for rental duration")
issue_details = st.text_input("Value for issue details")
date_submitted = st.text_input("Value for date (default is today)", value=datetime.today().strftime('%Y-%m-%d'))
status = st.selectbox("Value for status", ["active", "resolved", "pending"])

list_of_values = [
    client_id,
    rental_date,
    equipment_needed,
    rental_duration,
    issue_details,
    date_submitted,
    status,
]
with st.form("form"):
    submitted = st.form_submit_button("Add new ticket")

if submitted:
    conn._instance.execute(
        f"INSERT INTO {table_name} (client_id, rental_date, equipment_needed, rental_duration, issue_details, date_submitted, status) VALUES (?, ?, ?, ?, ?, ?, ?)",  # if you add more input values, add a question mark for each one
        list_of_values,
    )
    row_count = conn.query(
        f"SELECT COUNT(1) FROM {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )
    st.write(f"{table_name} now has {row_count.iat[0, 0]} rows.")
