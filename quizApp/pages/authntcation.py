import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from quizApp.dataBase import init_db
from quizApp.pages.User import User, Student, Teacher

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
        
        user = User.get_user_by_credentials(login_name, login_pass)
        
        if user:
            st.success("Login Successful!")
            
            st.session_state["current_user"] = user            
            if isinstance(user, Teacher):
                st.session_state["teacher_id"] = user.Uid
                st.session_state.role = user.role
                st.switch_page("pages/exams.py")
            else:
                st.switch_page("pages/teachers.py")
        else:
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
        user = User.get_user_by_credentials(username,password)
        
        if not user:
            if role == "student":
                new_user = Student(None, username, password)
            else:
                new_user = Teacher(None, username, password)
            
            Uid = User.insert_user(new_user)
            
            new_user.Uid = Uid
            
            st.success("success adding user")
            
            st.session_state["current_user"] = new_user
            
            if isinstance(new_user, Student):
                st.switch_page("pages/teachers.py")
            else:
                st.session_state["teacher_id"] = Uid
                st.switch_page("pages/exams.py")
        else:
            st.error("user exist")