import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

st.set_page_config(layout="wide")

if not st.session_state.get("logged_in"):
    st.switch_page("pages/authntcation.py")

with st.sidebar:
        if st.button("🚪 Logout"):
            st.session_state.clear()
            st.rerun()
st.title("🎓 Quiz System")