import streamlit as st
from data import util

st.title("Get premise by location")

st.warning("If you see errors, ensure you've created the table(s) first using the `Seed Data` pages.")

table_name = "premise"

conn = util.get_connection()
premise_df = conn.query(
    f"SELECT premise_location FROM {table_name}",
    ttl=0  # don't cache results so changes in the database are immediately retrieved
)
st.write("Available Premises for Search:")
st.dataframe(premise_df, use_container_width=True, hide_index=True)
value = st.text_input("Search for premise by location")

result_df = conn.query(
    f"select * from {table_name} where premise_location = :value",  # change "person" to your columnname
    params=dict(value=value),
    ttl=0,  # don't cache results so changes in the database are immediately retrieved
)
num_rows_found = len(result_df)
st.write(f'{num_rows_found} row{"" if num_rows_found == 1 else "s"} found for `{value}`')
st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True,
)
