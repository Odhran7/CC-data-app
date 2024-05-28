import streamlit as st
from data import util

st.title("Get invoices by status")

st.warning("If you see errors, ensure you've created the table(s) first using the `Seed Data` pages.")

table_name = "invoice"

conn = util.get_connection()
value = st.text_input("Status to search (paid, unpaid, refund, pending)")

result_df = conn.query(
    f"select * from {table_name} where status = :value", 
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
