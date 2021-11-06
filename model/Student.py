# -*- coding: utf-8 -*-

class Student:
    def __init__(self, student_id: int, s_name: str, s_gender: str, s_age: int, s_department: str, s_major: str):
        self.student_id = student_id  # 学生ID
        self.s_name = s_name  # 学生姓名
        self.s_gender = s_gender  # 学生性别
        self.s_age = s_age  # 学生年龄
        self.s_department = s_department  # 所属学院
        self.s_major = s_major  # 所属年级
