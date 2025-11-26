import sys
import os
#omar sayed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
init_db.createTables()
db = init_db.dbIns
username = st.text_input("username")
password = st.text_input("password",type="password")
role = st.radio("role",["stuednt","teacher"])
if st.button("sign up"):
    users = db.getAll("users")
    user = None
    for u in users:
        if u[1] == username:
            user = u
            break
    if not user:
        db.insert("users",{
            "userName" : username,
            "password" : password,
            "role" : role
        })
        st.success("success adding user")
        Uid = db.get("users",{"userName":username})[0][0]
        st.session_state["userID"] = Uid
        st.switch_page("/teachers.py")