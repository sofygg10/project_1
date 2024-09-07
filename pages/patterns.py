import streamlit as st
from patterns_db_helper import get_all_patterns
import pandas as pd

st.title("get all patterns")

patterns = get_all_patterns()

df = pd.DataFrame(patterns, columns = ["id", "name", "sku", "category", "price", "dificulty_level", "publication_date" ])
st.write(df) 



