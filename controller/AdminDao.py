# -*- coding: utf-8 -*-
from model import Student, Course, Admin, CourseRecord
import server.HBaseConnect
import model.StudentPassword
import model.ReturnValue as Value
# Operate State
SUCCESS = Value.SUCCESS
FAILURE = Value.FAILURE
INFO_ERROR = Value.INFO_ERROR


# TODO(添加学生信息：完成)
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
        return FAILURE


# TODO(添加课程表：完成)
def add_course(course: model.Course.Course):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table('Course')
        # Add course data
        table.put(course.course_id, {
            'CInfo:CourseID': course.course_id, 'CInfo:CName': course.course_name,
            'CInfo:Credit': course.credit, 'CInfo:Time': course.time,
            'Teaching:Teacher': course.teacher, 'Teaching:Title': course.title
        })
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE


# TODO(添加学生密码：完成)
def add_student_password(student_pwd: model.StudentPassword.StudentPassword):  # Add & Update Student Password
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        # Add Student Password
        table = connection.get_table('StudentPassword')
        table.put(student_pwd.student_id,
                  {'StudentID:': student_pwd.student_id,
                   'Password:': student_pwd.student_password})  # 单级列表添加要加”:“号（详细参考HappyBase文档说明）
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE


# TODO(删除学生信息和密码：完成)
def delete_student_info_and_pwd(sid: str):
    print(sid)
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table('Student')
        table.delete(sid)
        table = connection.get_table('StudentPassword')
        table.delete(sid)
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE


# TODO(修改学生信息：完成)
def edit_student(student: model.Student.Student):
    # Use function add_student
    return add_student(student)


# TODO(修改学生密码：完成)
def edit_student_pwd(aid: str, student_pwd: model.StudentPassword.StudentPassword):
    # Find the student
    return add_student_password(student_pwd)


# TODO(修改课程表：完成)
def edit_course(course: model.Course.Course):
    return add_course(course)


# TODO(删除选课信息：完成)
def delete_course_record(sid, cid):
    connection = server.HBaseConnect.HBaseConnect()
    new_id = cid + sid
    return connection.delete_table_row("CourseRecord", new_id)


# TODO(删除课程表：完成)
def delete_course(cid: str):
    connection = server.HBaseConnect.HBaseConnect()
    return connection.delete_table_row("Course", cid)


# TODO(修改管理员密码：完成)
def edit_admin_password(admin: model.Admin.Teacher, new_pwd: str):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        check_table = connection.get_table("Admin")
        check_data = check_table.row(admin.admin_id)
        if str(check_data[b'Password']) is not admin.password:
            connection.stop()
            return INFO_ERROR
        else:
            check_table.put(admin.admin_id, {'Password:':new_pwd})
            connection.stop()
            return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE


# TODO(修改选课信息（仅修改分数）：待完善)
def edit_course_record(course: model.CourseRecord):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table("CourseRecord")
        table.put()
    except Exception as e:
        print(e)
        return FAILURE


# TODO(管理员添加选课信息：待完善)
def add_course_record_admin(course: model.CourseRecord.CourseRecord):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table("CourseRecord")
        new_row = course.course_id + course.student_id
        table.put(new_row, {
            'CourseID:': course.course_id, 'StudentID:': course.student_id, 'Score:': course.score})
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE


# TODO(添加管理员（不开放）)
def add_admin(admin: model.Admin.Teacher):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table("Admin")
        table.put(admin.admin_id, {
            'AdminID:':admin.admin_id, 'AdminName:': admin.admin_name, 'Password:': admin.password
        })
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE
