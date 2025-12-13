import streamlit as st

st.title("My Website")

def show_aboutus_page():
    st.header="About us"
    st.write("This is about us page")

def show_internship_page():
    st.header="Internship"
    st.write("This is internship page")

def show_courses_page():
    st.header="Courses"
    st.write("This is courses page")

def show_fees_page():
    st.header="Fees"
    st.write("This is fees page")

if 'page' in st.session_state:
    st.session_state.page="About us"

with st.sidebar:
    if st.button("About us",width="stretch"):
        st.session_state.page="About us"
    if st.button("Internship",width="stretch"):
        st.session_state.page="Internship"
    if st.button("Courses",width="stretch"):
        st.session_state.page="Courses"
    if st.button("Fees",width="stretch"):
        st.session_state.page="Fees"  

if st.session_state.page=="About us":
    show_aboutus_page()
elif st.session_state.page=="Internship":
    show_internship_page()
elif st.session_state.page=="Courses":
    show_courses_page()
elif st.session_state.page=="Fees":
    show_fees_page()


   

