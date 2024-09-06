import streamlit as st 
import json
import os
from main import login_cookies


if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


def get_PATH():
    return os.getcwd()

def reload():
    st.query_params(reload=True)


# Display appropriate page based on login state
if st.session_state.logged_in:
    st.title("Welcome to the Homepage!")
    st.write("You are logged in.")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.switch_page('views/1Home.py')
else:
    with st.form("Login_form_box"):
        st.title("Login")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Submit"):
            creds_dict = {
                "username": username,
                "password": password,
            }
            with open('accounts.txt', 'r') as f:
                accounts = f.read().splitlines()
                for account in accounts:
                    credentials = json.loads(account)
                    if credentials["username"] == username and credentials["password"] == password:
                        st.session_state.logged_in = True
                        st.session_state.institute = credentials['Facility']
                        login_cookies(credentials)
                        st.success("Logged in successfully!")
                        st.switch_page('views/2Modules.py')
            st.error("Invalid credentials")
                
    with st.form("Signup_form"):
        st.title("Signup")
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        Facility = st.text_input("Facility")
        if st.form_submit_button("Submit"):
    
        # Here you would normally save the user's credentials securely
            with open('facilities.txt', 'r') as f:
                facilities = f.read().splitlines()
                for facility in facilities:
                    if Facility == facility:
                        credentials_json = {
                            "username": username,
                            "password": password,
                            "Facility": Facility,
                            }
                        with open('accounts.txt', 'a') as f:
                            json.dump(credentials_json, f)
            
                            st.success("User registered! Please log in.")
                            st.session_state.logged_in = True
                            st.switch_page('views/2Modules.py')
            st.error("Your facility is invalid. Sorry :(")