import  pandas as pd
import streamlit as st

st.title("CSV Uploader")

file=st.file_uploader("Upload a CSV file here",type=["csv"])

if file :
    df=pd.read_csv(file)
    st.dataframe(df)