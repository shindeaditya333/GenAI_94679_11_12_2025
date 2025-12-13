import streamlit as st

st.title("First Streamlit")
st.header("Just started..!")
st.write("This is my first streamlit program !")

if st.button("Start",type="primary"):
    st.toast("You clicked Start")