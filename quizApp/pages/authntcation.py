import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
init_db.createTables()

username = st.text_input("username")
password = st.text_input("password",type="password")
role = st.radio("role",["stuednt","teacher"])
if st.button("sign up"):
    st.write("button clicked")
    users = db.getAll("users")
    user = None
    for u in users:
        if u[1] == username:
            user = u
            break
    if not user:
        st.write("user not exist")
        Uid = db.insert("users",{
            "userName" : username,
            "password" : password,
            "role" : role
        })
        st.success("success adding user")
        st.session_state["userID"] = Uid
        st.switch_page("pages/teachers.py")
    else:
        st.error("user exist")
        