# -*- coding: utf-8 -*-
import model.Student
import server.HBaseConnect
import model.StudentPassword

# Operate State
SUCCESS = "SUCCESS"
FAILED = "FAILED"


def add_student(student: model.Student.Student):  # Add & Update Student Info
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table('Student')
        # Add student data
        table.put(student.student_id, {'SInfo:StudentID': student.student_id, 'SInfo:SName': student.s_name,
                                       'SInfo:SGender': student.s_gender, 'SInfo:SAge': student.s_age,
                                       'Studies:SDepartment': student.s_department,
                                       'Studies:SMajor': student.s_major})
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return e


def delete_student():
    pass


def edit_student():
    pass


def add_student_password(student_pwd: model.StudentPassword.StudentPassword):  # Add & Update Student Password
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        # Add Student Password
        table = connection.get_table('StudentPassword')
        table.put(student_pwd.student_id,
                  {'StudentID:': student_pwd.student_id, 'Password:': student_pwd.student_password})    # 单级列表添加要加”:“号（详细参考HappyBase文档说明）
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILED


def delete_student_info_and_pwd(sid: str):
    print(sid)
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table('Student')
        table.delete(sid)
        connection.stop()
        connection.start()
        table = connection.get_table('StudentPassword')
        table.delete(sid)
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILED


def delete_pwd(sid: str):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table('StudentPassword')
        table.delete(sid)
        connection.stop()
    except Exception as e:
        print(e)
        return e
