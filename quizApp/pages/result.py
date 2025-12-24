import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
import pandas as pd
db = init_db.dbIns

st.title("Result Analysis")

attid = st.session_state.get("attid")

query = """
    SELECT 
        q.QusID,
        q.header,
        uc.text AS user_answer,
        ca.text AS correct_answer
    FROM answers a
    JOIN qustions q ON q.QusID = a.QusID
    JOIN choices uc ON uc.ChID = a.ChID
    JOIN choices ca ON ca.QusID = q.QusID AND ca.correct = 1
    WHERE a.AttID = ? AND a.correctnes = 0
    """
params = (attid,)
wrong_answers = db.query(query,params)

if not wrong_answers:
    st.success("All answers are correct!")
    st.stop()

st.success(st.session_state.score)
st.markdown({f"## duration is {st.session_state.duration}"})
for i, row in enumerate(wrong_answers, start=1):
    qus_id, question, user_ans, correct_ans = row

    st.markdown(f"### Question {i}")
    st.write(question)

    st.markdown(f" **Your Answer:** {user_ans}")
    st.markdown(f" **Correct Answer:** {correct_ans}")

    st.divider()
    
    if st.button("back to exams"):
        del st.session_state.duration
        del st.session_state.score
        del st.session_state.attid
        st.switch_page("pages/exams.py")