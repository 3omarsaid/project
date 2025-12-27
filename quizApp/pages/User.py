import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db

db = init_db.dbIns

class User:
    def __init__(self, Uid, userName, password):
        self.Uid = Uid
        self.userName = userName
        self.password = password
    
    @property
    def role(self):
        """Returns the role of the user"""
        return "user"
    
    def to_dict(self):
        """Convert user object to dictionary for database operations"""
        return {
            "userName": self.userName,
            "password": self.password,
            "role": self.role
        }
    
    @staticmethod
    def from_tuple(data):
        """Create User object from database tuple (Uid, userName, password, role)"""
        if len(data) < 4:
            return None
        
        Uid, userName, password, role = data[0], data[1], data[2], data[3]
        
        if role == "student":
            return Student(Uid, userName, password)
        elif role == "teacher":
            return Teacher(Uid, userName, password)
        else:
            return User(Uid, userName, password)

    def get_user_by_credentials(username, password):      
        users = db.getAll("users")
        for user_data in users:
            if user_data[1] == username and user_data[2] == password:
                return User.from_tuple(user_data)
        return None
    
    def insert_user(user_obj):
        return db.insert("users", user_obj.to_dict())

class Student(User):
    def __init__(self, Uid, userName, password):
        super().__init__(Uid, userName, password)
    
    @property
    def role(self):
        """Returns 'student' role"""
        return "student"

class Teacher(User):
    def __init__(self, Uid, userName, password):
        super().__init__(Uid, userName, password)
    
    @property
    def role(self):
        """Returns 'teacher' role"""
        return "teacher"