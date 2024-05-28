import streamlit as st

# Helper functions
def group_project_modify_info_footer(text, icon):
    st.info(f"{text}", icon=icon)
    st.write("\n")

st.set_page_config(
    page_title="INFOSYS220 streamlit exercises",
)

st.header("Data App Final Deliverable")

st.subheader("UC#1 F#3 - Edit Pricing")
st.write("View all titles of premises and view their recommended pricing")
group_project_modify_info_footer("You will use this to edit pricing", "💰")
st.write("\n")

st.subheader("UC #2 F#1 - View Premise Details")
st.write("View all details of a premise")
group_project_modify_info_footer("You will use this to view premise details", "🏠")
st.write("\n")

st.subheader("UC#3 F#2 - Request Human Support")
st.write("Request human support for a specific listing")
group_project_modify_info_footer("You will use this to request human support", "🤝")
st.write("\n")

st.subheader("UC#4 F#1 - Facilitate Messaging")
st.write("Create a new message")
group_project_modify_info_footer("You will use this to facilitate messaging", "📧")

st.subheader("UC#5 F#1 - Manage Transactions")
st.write("Manage all transactions including invoices & refunds")
group_project_modify_info_footer("You will use this to manage transactions", "💸")

st.subheader("UC #6 F#3 - Apply Discount")
st.write("Allows verification of a discount code")
group_project_modify_info_footer("You will use this to validate and apply discounts", "🏷️")
