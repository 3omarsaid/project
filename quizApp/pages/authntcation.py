import sys
import os
# بظبط المسار عشان اقدر استدعي ملفات الداتابيز
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import streamlit as st
from quizApp.dataBase import init_db

# بنعمل اوبجيكت من الداتابيز ونتأكد ان الجداول معمولة
db = init_db.dbIns
init_db.createTables()

st.title("Welcome to Quiz App")

# عملت تابين عشان افصل التسجيل عن الدخول ويبقى الشكل منظم
tab1, tab2 = st.tabs(["Sign In (دخول)", "Sign Up (حساب جديد)"])

# ==========================================
# Tab 1: Login Code (ده الجزء الجديد)
# ==========================================
with tab1:
    st.header("Login")
    
    # باخد البيانات من اليوزر عشان يدخل
    # حطيت key عشان ميحصلش تداخل مع ال inputs التانية
    login_name = st.text_input("Username", key="login_name")
    login_pass = st.text_input("Password", type="password", key="login_pass")
    
    if st.button("Login", key="login_btn"):
        # بجيب كل اليوزرز من الداتابيز عشان ادور فيهم
        users = db.getAll("users")
        found = False
        
        for u in users:
            # u[1] هو الاسم و u[2] هو الباسورد زي ما موجود في init_db
            if u[1] == login_name and u[2] == login_pass:
                found = True
                st.success("Login Successful!")
                
                # بحفظ الايدي بتاع اليوزر عشان استخدمه في باقي الصفحات
                st.session_state["userID"] = u[0]
                
                # بشوف هو مدرس ولا طالب عشان اوجهه للصفحة الصح
                # u[3] هو ال role
                if u[3] == "teacher":
                    st.switch_page("pages/exams.py")
                else:
                    # لو طالب وديه على صفحة الطلبة (لازم تكون عامل الملف ده)
                    # لو مفيش ملف للطلبة لسه، ممكن توجهه لأي صفحة تانية مؤقتا
                    st.switch_page("pages/teachers.py") 
                break
        
        if not found:
            st.error("Wrong Username or Password")


# ==========================================
# Tab 2: Sign Up Code (الكود القديم بتاعك)
# ==========================================
with tab2:
    st.header("Create Account")
    
    # نفس الكود بتاعك بالظبط بس حطيته هنا
    username = st.text_input("username", key="signup_user")
    password = st.text_input("password", type="password", key="signup_pass")
    role = st.radio("role", ["student", "teacher"], key="signup_role") # صلحت بس كلمة student
    
    if st.button("sign up", key="signup_btn"):
        st.write("button clicked")
        users = db.getAll("users")
        user = None
        
        # بتأكد ان الاسم مش متكرر
        for u in users:
            if u[1] == username:
                user = u
                break
        
        if not user:
            # لو مش موجود بضيفه في الداتابيز
            Uid = db.insert("users", {
                "userName" : username,
                "password" : password,
                "role" : role
            })
            st.success("success adding user")
            
            # بسجله دخول علطول بعد ما عمل اكونت
            st.session_state["userID"] = Uid
            
            # بوجهه لصفحة المدرسين زي ما كان مكتوب
            st.switch_page("pages/teachers.py")
        else:
            st.error("user exist")