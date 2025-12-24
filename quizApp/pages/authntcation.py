import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from quizApp.dataBase import init_db

db = init_db.dbIns
init_db.createTables()

st.title("Welcome to Quiz App")

tab1, tab2 = st.tabs(["Sign In (دخول)", "Sign Up (حساب جديد)"])

with tab1:
    st.header("Login")
    
    login_name = st.text_input("Username", key="login_name")
    login_pass = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Login", key="login_btn"):
        st.session_state.logged_in = True
        users = db.getAll("users")
        found = False
        
        for u in users:
            if u[1] == login_name and u[2] == login_pass:
                found = True
                st.success("Login Successful!")
                
                st.session_state["userID"] = u[0]
                
                if u[3] == "teacher":
                    st.session_state["teacher_id"] = u[0]
                    st.session_state.role = u[3]
                    st.switch_page("pages/exams.py")
                else:
                    st.session_state.role = u[3]
                    st.switch_page("pages/teachers.py")
                break
        
        if not found:
            st.error("Wrong Username or Password")

with tab2:
    st.header("Create Account")
    st.session_state.logged_in = True

    username = st.text_input("username", key="signup_user")
    password = st.text_input("password", type="password", key="signup_pass")
    role = st.radio("role", ["student", "teacher"], key="signup_role") 

    if st.button("sign up", key="signup_btn"):
        st.write("button clicked")
        users = db.getAll("users")
        user = None
        
        for u in users:
            if u[1] == username:
                user = u
                break
        
        if not user:
            Uid = db.insert("users", {
                "userName" : username,
                "password" : password,
                "role" : role
            })
            st.success("success adding user")
            
            if(role == "student"):
                st.session_state["userID"] = Uid
                st.session_state.role = role
                st.switch_page("pages/teachers.py")
            else:
                st.session_state["teacher_id"] = Uid
                st.session_state.role = role
                st.switch_page("pages/exams.py")
        else:
            st.error("user exist")