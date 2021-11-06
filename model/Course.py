# -*- coding: utf-8 -*-
import datetime


class Course:
    def __init__(self, course_id: int, course_name: str, credit: int, time: datetime, teacher: str, title: str):
        self.course_id = course_id
        self.course_name = course_name
        self.credit = credit
        self.time = time
        self.teacher = teacher
        self.title = title

