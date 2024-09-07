import streamlit as st
import pandas as pd 
from patterns_db_helper import insert_patterns_in_bulk
from customers_db_helper import insert_customers_in_bulk

st.title("Upload data")

def extract_data_from_excel(patterns_file, customers_file):
    try:
        df = pd.read_excel(patterns_file)
        cs = pd.read_excel(customers_file)
    except Exception as e:
        st.write(f"Error reading the excel file: {e}")
        return[]    

    df = df.rename(columns={
        'Pattern Name': 'name',
        'SKU': 'sku',
        'Category': 'category',
        'Price (USD)': 'price',
        'Difficulty Level': 'dificulty_level',
        'Publication Date': 'publication_date'
    })

    df['publication_date']= pd.to_datetime(df["publication_date"])
    df['publication_date'] = df['publication_date'].dt.strftime('%Y-%m-%d')
    df['price']= df['price'].astype(float)

    insert_patterns_in_bulk(df)

    cs = cs.rename(columns={
        'Full name': 'name',
        'Email Address': 'email',
        'Registration Date': 'registration_date',
        'Country': 'country',
        'SKU': 'purchased_pattern_sku'
    })

    cs['registration_date']= pd.to_datetime(cs["registration_date"])
    cs['registration_date'] = cs['registration_date'].dt.strftime('%Y-%m-%d')

    insert_customers_in_bulk(cs)

    df_merged = pd.merge(cs, df, left_on='purchased_pattern_sku', right_on='sku', how='left')

    st.write(df_merged)

patterns_file = st.file_uploader("Upload the patterns excel file", type=["xls","xlsx"])
customers_file = st.file_uploader("Upload the customers excel file", type=["xls","xlsx"])

if st.button("Upload data"):
    if patterns_file is not None and customers_file is not None:
        extract_data_from_excel(patterns_file, customers_file)