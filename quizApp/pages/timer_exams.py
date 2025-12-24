import streamlit as st
import time

def Qus_countdown_timer(duration):
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = time.time()

    elapsed = time.time() - st.session_state.timer_start
    remaining = max(0, duration - elapsed)

    progress = remaining / duration
    st.progress(progress)

    if remaining <= 0:
        st.session_state.timer_done = True
    return remaining

def exam_timer_autoupdate(total_time):
    if "exam_start" not in st.session_state:
        st.session_state.exam_start = time.time()

    timer_box = st.empty()

    elapsed = time.time() - st.session_state.exam_start
    remaining = max(0, total_time - elapsed)
    progress = remaining / total_time

    with timer_box:
        st.progress(progress)

    if remaining <= 0:
        st.session_state.exam_finished = True
    return remaining