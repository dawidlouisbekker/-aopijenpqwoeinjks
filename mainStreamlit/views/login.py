import streamlit as st
import json
import time
import requests

def verify_recaptcha(response):
    secret_key = ''
    payload = {'secret': secret_key, 'response': response}
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    return r.json()


with st.form("Login_form_box"):
        st.title("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
       # st.markdown("""
   # <script src="https://www.google.com/recaptcha/api.js"></script>
   # <form action="?" method="POST">
   #     <div class="g-recaptcha" data-sitekey="key"></div>
    #</form>
#""", unsafe_allow_html=True)
        if st.form_submit_button("Submit"):
            verify_recaptcha()
            with open('Attempts.txt', 'a+') as f:
                json_data = {
                    'email': email,
                    'time': time.time()
                }
                json.dump(json_data, f)
                f.write('\n')
                attempts = f.read().splitlines()
                for attempt in attempts:
                    attempt_data = json.loads(attempt)
                    if attempt_data['time'] > (time.time()//1):
                        st.session_state.attempts_per_sec += 1
                if st.session_state.attempts_per_sec > 3:
                    st.write('DDOS')
                    st.stop()
                    
            creds_dict = {
                "username": email,
                "password": password,
            }
            
            with open('accounts.txt', 'r') as f:
                accounts = f.read().splitlines()
                for account in accounts:
                    credentials = json.loads(account)
                    if credentials["username"] == email and credentials["password"] == password:
                        st.session_state.logged_in = True
                        st.session_state.institute = credentials['Facility']
                        st.success("Logged in successfully!")
                        st.switch_page('views/2Modules.py')
            st.error("Invalid credentials")
