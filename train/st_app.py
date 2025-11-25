import streamlit as st

st.title("أهلاً بيك في Streamlit! 👋")

name = st.text_input("اكتب اسمك:")
age = st.number_input("اكتب سنّك:", min_value=1, max_value=120)

if st.button("اعرض الرسالة"):
    st.success(f"مرحباً {name}! سنّك هو {int(age)} سنة.")