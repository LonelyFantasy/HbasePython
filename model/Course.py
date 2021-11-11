# -*- coding: utf-8 -*-
import datetime


class Course:
    def __init__(self, course_id: str, course_name: str, credit: str, time: str, teacher: str, title: str):
        self.course_id = course_id  # 课程ID
        self.course_name = course_name  # 课程名称
        self.credit = credit    # 课程学分
        self.time = time    # 课程持续时间
        self.teacher = teacher  # 授课老师
        self.title = title  # 授课标题

