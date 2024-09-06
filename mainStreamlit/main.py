import streamlit as st
from streamlit_cookies_controller import CookieController


@st.dialog('Do you want to stay signed in on this device?')
def login_cookies(credentials):
    with st.form('cookies_form'):
        if st.form_submit_button('yes'):
            get_cookies().set('Credentials', credentials)
            st.write(get_cookies.getAll())
        

def get_cookies():
    cookies = CookieController()
    return cookies

if 'Serving' not in st.session_state:
    st.session_state.Serving = True

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'institute' not in st.session_state:
    st.session_state.institute = 'Eduvos'

if 'module' not in st.session_state:
    st.session_state.module = 'ITAIA'
    
#For AWS lambda
#from fastapi import FastAPI
#from mangum import Mangum
#app = FastAPI()
#handler = Mangum(app)    
#if __name__ == '__main__':
#    port = 80
#    print(f'Running the FastAPI server on port {port}')
#    uvicorn.run(app, host='0.0.0.0', port=port)


def get_module():
    module = st.session_state.module
    return module

def set_module(module : str):
    st.session_state.module = module
    
def set_institute(Institute : str):
    st.session_state.institute = Institute

def get_institute():
    institute = st.session_state.institute
    return institute
    
login_page = st.Page(
    page='views/login.py',
    title='Login',
    default=True,
)

sign_up_page = st.Page(
    page='views/signup.py',
    title='Signup',
    default=False,
)

logout_page = st.Page(
    page='views/logout.py',
    title='Logout',
    default=False,
)

Home_page = st.Page(
    page='views/1Home.py',
    title='Home',
    icon=':material/account_circle:',
)

Modules_page = st.Page(
   page='views/2Modules.py',
    title='Modules',
    icon=':material/extension:',
    default=False,
)

ChatBot_page = st.Page(
    page='views/3ChatBot.py',
    title='ChatBot',
    icon=':material/chat:',
    default=False,
)

ddos_page = st.Page(
    page='views/ddos.py',
    title='ddos',
    icon=':material/extension:',
    default=True,
)

if 'attempts_per_sec' not in st.session_state:
    st.session_state.attempts_per_sec = 0
if st.session_state.Serving:
    if st.session_state.logged_in != True:
        pg = st.navigation(pages={
        'Home': [login_page, sign_up_page],
        'Main': [Modules_page, ChatBot_page],
        })
    
#navigation
    else:
        pg = st.navigation(pages={
        'Home': [logout_page],
        'Main': [Modules_page, ChatBot_page],
        })
else: 
    
    pg = st.navigation(pages=[ddos_page])
    st.stop()


#run
pg.run()