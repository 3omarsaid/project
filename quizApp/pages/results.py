import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
from quizApp.pages.User import Student, Teacher
import pandas as pd

db = init_db.dbIns

current_user = st.session_state.get("current_user")

if not current_user:
    st.error("Please login first")
    st.switch_page("pages/authntcation.py")
    st.stop()

tap1, tap2 = st.tabs(["table", "dashboard"])

with tap1:
    if isinstance(current_user, Teacher):
        where = "a.TchID"
        name = "Stu"
        params = (current_user.Uid,)
    else:
        where = "a.StuID"
        name = "Tch"
        params = (current_user.Uid,)
    
    query = f"""
    select {name}.userName, e.title, a.score,a.numQus,a.duration_S,a.total_time,a.start_at from attempts a
    join exams e on e.ExID = a.Exid
    join users Tch on Tch.Uid = a.Tchid
    join users Stu on Stu.Uid = a.StuID
    where {where} = ?
    """

    result = db.query(query, params)
    df = pd.DataFrame(result, columns=['student name' if name == "Stu" else 'teacher name', 'Exam Title', 'Score', 'numQus', 'Duration', 'total time', 'Attempt Date'])
    st.dataframe(df)

with tap2:
    st.title("Attempts Dashboard")
    
    if isinstance(current_user, Student):
        st.subheader("Your Exam Performance")
    if isinstance(current_user, Teacher):
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
    col1, col2 = st.columns([1, 1])
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