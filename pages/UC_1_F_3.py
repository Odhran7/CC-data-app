import streamlit as st
from data import util

st.title("Get recommended price by title")

st.warning("If you see errors, ensure you've created the table(s) first using the `Seed Data` pages.")

table_name = "listing_price"

conn = util.get_connection()

# View rows to see
listings_df = conn.query(
    f"SELECT listing_title FROM {table_name}",
    ttl=0  # don't cache results so changes in the database are immediately retrieved
)

st.write("Available Premises for Search:")
st.dataframe(listings_df, use_container_width=True, hide_index=True)
value = st.text_input("Title to search")

result_df = conn.query(
    f"select * from {table_name} where listing_title = :value",  # change "person" to your columnname
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
