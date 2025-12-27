import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
import pandas as pd
db = init_db.dbIns

from pages.timer_exams import format_time
st.title("Result Analysis")

attid = st.session_state.get("attid")

query = """
    SELECT 
        q.QusID,
        q.header,
        CASE 
            WHEN a.ChID IS NULL THEN 'No answer (time expired)'
            ELSE uc.text
        END AS user_answer,
        ca.text AS correct_answer
    FROM answers a
    JOIN qustions q ON q.QusID = a.QusID
    LEFT JOIN choices uc ON uc.ChID = a.ChID
    JOIN choices ca ON ca.QusID = q.QusID AND ca.correct = 1
    WHERE a.AttID = ? AND a.correctnes = 0
    """
params = (attid,)
wrong_answers = db.query(query,params)

if not wrong_answers:
    st.success("All answers are correct!")
    st.info(f"**Score:** {st.session_state.score}")
    st.info(f"**Duration:** {format_time(st.session_state.duration)}")
    if st.button("back to exams"):
        st.session_state.pop("duration", None)
        st.session_state.pop("score", None)
        st.session_state.pop("attid", None)
        st.switch_page("pages/exams.py")
    st.stop()

st.success(f"Your Score: {st.session_state.score}")
st.info(f"**Duration:** {format_time(st.session_state.duration)}")
st.markdown(f"---")
st.markdown(f"### Wrong Answers Review")

for i, row in enumerate(wrong_answers, start=1):
    qus_id, question, user_ans, correct_ans = row

    st.markdown(f"#### Question {i}")
    st.write(question)

    st.markdown(f"**Your Answer:** {user_ans}")
    st.markdown(f"**Correct Answer:** {correct_ans}")

    st.divider()
    
if st.button("back to exams"):
    st.session_state.pop("duration", None)
    st.session_state.pop("score", None)
    st.session_state.pop("attid", None)
    st.switch_page("pages/exams.py")