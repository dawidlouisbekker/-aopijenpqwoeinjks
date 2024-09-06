import streamlit as st
import json
import random
import time
def create_email_auth_data(email) -> bool:
    code = [random.randint(0, 9) for _ in range(6)]
    attempts = 0
    with open('AccountReg.txt', 'r') as f:
        auth_json = {
            "email": email,
            "code": code,
            "Attempts": attempts
        }
        json.dumps(auth_json + '\n', f)
        f.close()
        
    
    

with st.form("Signup_form"):
    st.title("Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    Facility = st.text_input("Facility")
    if st.form_submit_button("Submit"):
        with open('Attempts.txt', 'a') as f:
            f.write(email, time.time())
        with open('validEmails.txt', 'r') as f:
            emails = f.read().splitlines()
            for email in emails:
                if email == email:

        # Here you would normally save the user's credentials securely
                    #with open('facilities.txt', 'r') as f:
                    #facilities = f.read().splitlines()
                    #    for facility in facilities:
                    #    if Facility == facility:
                    credentials_json = {
                        "email": email,
                        "password": password,
                        "Facility": Facility,
                        }
                    create_email_auth_data(email)
                    code = st.text_input("Enter code sent to " + email)
                    if st.button('Submit'):
                        with open('AccountReg.txt', 'r') as f:
                            attempts = f.read().splitlines()
                            for attempt in attempts:
                                data = json.loads(attempt)
                                if data["code"] == code:
                                    with open('accounts.txt', 'a') as f:
                                        json.dump(credentials_json, f)
                                    st.session_state.logged_in = True
                                    st.session_state.institute = data['Facility']
                                    st.success("Logged in successfully!")
                                    st.switch_page('views/2Modules.py')
                                else:
                                    if data["Attempts"] == 3:
                                        st.error("Too many attempts retry signup")
                                    else:
                                        st.error("Wrong code. Please try again.")
                                        data["Attempts"] += 1
                                    
                st.error("Your facility is invalid. Sorry :(")                    
            st.error('Your Email may not signup')     
                

