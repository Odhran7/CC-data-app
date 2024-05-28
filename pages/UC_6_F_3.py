import streamlit as st
from data import util
import pandas as pd

st.title("Get Valid Discounts")
st.warning("If you see errors, ensure you've created the table(s) first using the Seed Data pages.")

table_name = "discount"

conn = util.get_connection()

valid_discounts_only = st.checkbox("Show only valid discounts")

current_date = pd.Timestamp.now().strftime('%Y-%m-%d')
query = f"""
    SELECT *,
    CASE
        WHEN discount_value > 0 AND expiry_date >= '{current_date}' THEN 'valid'
        ELSE 'invalid'
    END as is_valid
    FROM {table_name}
"""

result_df = conn.query(query, ttl=0)

if valid_discounts_only:
    result_df = result_df[result_df['is_valid'] == 'valid']
else:
    result_df = result_df[result_df['is_valid'] == 'invalid']

num_rows_found = len(result_df)
validity_status = "valid" if valid_discounts_only else "invalid"
st.write(f'{num_rows_found} {validity_status} discount code{"" if num_rows_found == 1 else "s"} found')
st.dataframe(
    result_df,
    use_container_width=True,
    hide_index=True,
)
