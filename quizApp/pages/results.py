import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
import pandas as pd
db = init_db.dbIns
role = st.session_state.role

tap1, tap2 = st.tabs(["table","dashboard"])

with tap1:
    if role == "teacher":
        where = "a.TchID"
        name = "Stu"
        tchid= st.session_state["teacher_id"]
        params = (tchid,)
    else:
        where = "a.StuID"
        name = "Tch"
        stuid = st.session_state["userID"]
        params = (stuid,)
    query = f"""
    select {name}.userName, e.title, a.score,a.numQus,a.duration_S,a.total_time,a.start_at from attempts a
    join exams e on e.ExID = a.Exid
    join users Tch on Tch.Uid = a.Tchid
    join users Stu on Stu.Uid = a.StuID
    where {where} = ?
    """

    result =db.query(query,params)
    df=pd.DataFrame(result,columns=[ 'student name'if name == "Stu" else 'teacher name' ,'Exam Title','Score','numQus','Duration','total time','Attempt Date'])
    st.dataframe(df)

with tap2:
    st.title("Attempts Dashboard")
    
    if role == "student":
        st.subheader("Your Exam Performance")
    if role == "teacher":
        st.subheader("Overview of exams AVG scores")

        st.bar_chart(
            df.groupby("Exam Title")["Score"].mean()
        )
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Attempts", len(df))

    with col2:
        st.metric("Average Score", round(df["Score"].mean(), 2))

    with col3:
        st.metric("Highest Score", df["Score"].max())
    col1 , col2 = st.columns([1,1])
    with col1:
        st.subheader("Score Distribution")

        st.bar_chart(
            df["Score"].value_counts().sort_index()
        )
    with col2:
        st.subheader("Score Over Time")

        df["Attempt Date"] = pd.to_datetime(df["Attempt Date"])

        st.line_chart(
            df.set_index("Attempt Date")["Score"]
        )

if st.button("back to exams"):
    st.switch_page("pages/exams.py")