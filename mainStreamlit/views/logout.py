import streamlit as st

st.title("Welcome to the Homepage!")
st.write("You are logged in.")
if st.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page('views/2Modules.py')