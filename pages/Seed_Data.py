import streamlit as st
from data import util

st.title("Data seeding example")

with st.form("form"):
    submitted = st.form_submit_button("Seed data")

if submitted:
    conn = util.get_connection()


    # UC#6 F#3 - Apply Discount
    columns = ["discount_id", "discount_value", "expiry_date"]
    data = [
        {"discount_id": "1", "discount_value": "10", "expiry_date": "2024-06-01"},
        {"discount_id": "2", "discount_value": "20", "expiry_date": "2023-12-31"},
        {"discount_id": "3", "discount_value": "0", "expiry_date": "2024-01-15"},
        {"discount_id": "4", "discount_value": "15", "expiry_date": "2024-07-01"},
        {"discount_id": "5", "discount_value": "5", "expiry_date": "2023-11-30"}
    ]
    table_name = util.create_seed_data(conn, "discount", columns, data)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

    # UC#5 F#1 - Manage Transaction
    columns = ["invoice_id", "billing_date", "amount", "status"]
    data = [
        {"invoice_id": "1", "billing_date": "2024-06-01", "amount": "100.00", "status": "paid"},
        {"invoice_id": "2", "billing_date": "2023-12-31", "amount": "150.00", "status": "unpaid"},
        {"invoice_id": "3", "billing_date": "2024-01-15", "amount": "200.00", "status": "paid"},
        {"invoice_id": "4", "billing_date": "2024-07-01", "amount": "250.00", "status": "unpaid"},
        {"invoice_id": "5", "billing_date": "2023-11-30", "amount": "300.00", "status": "paid"},
        {"invoice_id": "6", "billing_date": "2023-11-30", "amount": "320.00", "status": "refund"},
        {"invoice_id": "7", "billing_date": "2023-11-31", "amount": "400.00", "status": "pending"}
    ]
    table_name = util.create_seed_data(conn, "invoice", columns, data)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

    # UC#3 F#2 - Request Human Support

    columns = ["client_id", "rental_date", "equipment_needed", "rental_duration", "issue_details", "date_submitted", "status"]
    data = [
        {"client_id": "1", "rental_date": "2024-05-01", "equipment_needed": "Projector", "rental_duration": "2 days", "issue_details": "None", "date_submitted": "2024-05-01", "status": "active"},
        {"client_id": "2", "rental_date": "2024-05-02", "equipment_needed": "Laptop", "rental_duration": "1 week", "issue_details": "Battery issue", "date_submitted": "2024-05-02", "status": "pending"},
        {"client_id": "3", "rental_date": "2024-05-03", "equipment_needed": "Sound System", "rental_duration": "3 days", "issue_details": "Broken cable", "date_submitted": "2024-05-03", "status": "resolved"},
        {"client_id": "4", "rental_date": "2024-05-04", "equipment_needed": "Microphone", "rental_duration": "1 day", "issue_details": "No sound", "date_submitted": "2024-05-04", "status": "active"},
        {"client_id": "5", "rental_date": "2024-05-05", "equipment_needed": "Camera", "rental_duration": "5 days", "issue_details": "Lens issue", "date_submitted": "2024-05-05", "status": "pending"}
    ]
    table_name = util.create_seed_data(conn, "support", columns, data)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

    # UC #1 F#3 - Edit Pricing
    columns = ["listing_id", "listing_title", "price", "recommended_price"]
    data = [
         {"listing_id": "1342", "listing_title": "Premium Commercial Kitchen", "price": "450.00", "recommended_price": "500.00"},
        {"listing_id": "1", "listing_title": "Downtown Commercial Kitchen", "price": "1500.00", "recommended_price": "1600.00"},
        {"listing_id": "2", "listing_title": "Suburban Bakery Kitchen", "price": "1200.00", "recommended_price": "1300.00"},
        {"listing_id": "3", "listing_title": "Industrial Kitchen Space", "price": "2000.00", "recommended_price": "2100.00"},
        {"listing_id": "4", "listing_title": "Small Cafe Kitchen", "price": "800.00", "recommended_price": "850.00"},
        {"listing_id": "5", "listing_title": "Large Restaurant Kitchen", "price": "2500.00", "recommended_price": "2600.00"}
    ]

    table_name = util.create_seed_data(conn, "listing_price", columns, data)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

    # UC#4 F#1 - Facilitate Messaging
    columns = ["userHostID", "userTenantID", "message", "datetime"]
    data = [
        {"userHostID": "101", "userTenantID": "201", "message": "Hello, I would like to inquire about the availability.", "datetime": "2024-05-01 10:00:00"},
        {"userHostID": "101", "userTenantID": "202", "message": "Is the kitchen available for a week?", "datetime": "2024-05-01 11:00:00"},
        {"userHostID": "102", "userTenantID": "203", "message": "Can I book the kitchen for a weekend event?", "datetime": "2024-05-02 09:30:00"},
        {"userHostID": "103", "userTenantID": "204", "message": "What is the price for a two-day rental?", "datetime": "2024-05-02 14:00:00"},
        {"userHostID": "104", "userTenantID": "205", "message": "Do you offer any discounts for long-term rentals?", "datetime": "2024-05-03 16:45:00"}
    ]

    table_name = util.create_seed_data(conn, "message", columns, data)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

    #UC#2 F#1 - View Premise Details
    columns = ["listingID", "premise_title", "premise_description", "premise_location", "star_rating"]
    data = [
    {"listingID": "1", "premise_title": "Downtown Commercial Kitchen", "premise_description": "A fully equipped commercial kitchen located in the heart of downtown.", "premise_location": "123 Main St, Downtown", "star_rating": "4.5"},
    {"listingID": "2", "premise_title": "Suburban Bakery Kitchen", "premise_description": "A cozy bakery kitchen perfect for small scale baking operations.", "premise_location": "456 Oak St, Suburbia", "star_rating": "4.0"},
    {"listingID": "3", "premise_title": "Industrial Kitchen Space", "premise_description": "Spacious industrial kitchen suitable for large scale food production.", "premise_location": "789 Industrial Ave, Industrial Park", "star_rating": "4.7"},
    {"listingID": "4", "premise_title": "Small Cafe Kitchen", "premise_description": "A small, intimate kitchen perfect for cafe operations.", "premise_location": "101 Cafe Blvd, Midtown", "star_rating": "4.2"},
    {"listingID": "5", "premise_title": "Large Restaurant Kitchen", "premise_description": "A large restaurant kitchen with top-notch equipment and ample space.", "premise_location": "202 Restaurant Rd, Uptown", "star_rating": "4.8"}
    ]
    table_name = util.create_seed_data(conn, "premise", columns, data)

    result_df = conn.query(
        f"select * from {table_name}",
        ttl=0,  # don't cache results so changes in the database are immediately retrieved
    )

    st.write("Table created:")
    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True,
    )

    ###################################################################################
    # To create multiple tables in a single page/form, uncomment the lines below and
    # change the REPLACEME part.
    ###################################################################################

    # table_name = util.create_seed_data_REPLACEME2(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )

    # table_name = util.create_seed_data_REPLACEME3(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )

    # table_name = util.create_seed_data_REPLACEME4(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )

    # table_name = util.create_seed_data_REPLACEME5(conn)
    # result_df = conn.query(
    #     f"select * from {table_name}",
    #     ttl=0,  # don't cache results so changes in the database are immediately retrieved
    # )
    # st.write("Table created:")
    # st.dataframe(
    #     result_df,
    #     use_container_width=True,
    #     hide_index=True,
    # )


# Function to seed UC#6

