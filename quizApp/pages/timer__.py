import streamlit as st
import time

def countdown_progress_bar(duration_seconds):
    """
    """
    st.title("")

    #  
    progress_bar = st.progress(1.0)
    status_text = st.empty()

    start_time = time.time()
    end_time = start_time + duration_seconds

    with st.spinner(""):
        while True:
            current_time = time.time()
            remaining_time = end_time - current_time

            if remaining_time <= 0:
                break

            #   
            progress_ratio = remaining_time / duration_seconds

            #  
            progress_bar.progress(progress_ratio)
            status_text.text(f"{int(remaining_time) + 1} ")

            time.sleep(0.1)  # 

    # 
    progress_bar.progress(0)
    status_text.success()


#  Streamlit
st.sidebar.header(")

duration = st.sidebar.number_input(
    
    min_value=1,
    max_value=600,
    value=30,
    step=1
)

if st.sidebar.button(""):
    countdown_progress_bar(duration)