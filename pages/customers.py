import streamlit as st
from customers_db_helper import get_all_customers
import pandas as pd

st.title("get all custommers")

customers = get_all_customers()

df = pd.DataFrame(customers, columns = ["id", "name", "email", "registration_date", "country", "purchased_pattern_sku", "pattern_name", "pattern_category", "pattern_price", "pattern_level", "pattern_publication" ])

st.write(df)

