import streamlit as st
import time

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

def Qus_countdown_timer(duration):
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = time.time()

    elapsed = time.time() - st.session_state.timer_start
    remaining = max(0, duration - elapsed)

    progress = remaining / duration
    
    time_str = format_time(remaining)
    if remaining <= 10:
        st.error(f"Time remaining: {time_str}")
    elif remaining <= 30:
        st.warning(f"Time remaining: {time_str}")
    else:
        st.info(f"Time remaining: {time_str}")
    
    st.progress(progress)

    if remaining <= 0:
        st.session_state.timer_done = True
    return remaining

def exam_timer_autoupdate(total_time):
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = time.time()

    timer_box = st.empty()

    elapsed = time.time() - st.session_state.timer_start
    remaining = max(0, total_time - elapsed)
    progress = remaining / total_time

    with timer_box:
        time_str = format_time(remaining)
        if remaining <= 60:
            st.error(f"Exam time remaining: {time_str}")
        elif remaining <= 300:
            st.warning(f"Exam time remaining: {time_str}")
        else:
            st.info(f"Exam time remaining: {time_str}")
        st.progress(progress)

    if remaining <= 0:
        st.session_state.exam_finished = True
    return remaining