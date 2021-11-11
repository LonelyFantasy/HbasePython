from flask import Flask, request, Response

import controller.AdminDao
import controller.StudentDao
import model.StudentPassword
from controller.BasicDao import login_check
from model import Course, Student, CourseRecord, Admin

# Operate State
SUCCESS = "SUCCESS"
FAILED = "FAILURE"

app = Flask(__name__)


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/index', methods=['post', 'get'])
def hello_world():  # put application's code here
    return 'Hello World!'


# TODO(接口：登陆：待完善)
@app.route('/login', methods=['post'])
def login():
    # Get login form
    userid = request.form.get("id")
    pwd = request.form.get("password")
    user_type = request.form.get("user_type")
    result = login_check(str(userid), pwd, int(user_type))
    return "data"


# TODO(接口：添加学生信息和密码：完成)
@app.route('/addStudent', methods=['post'])
def add_student():
    # Get student form
    student = model.Student.Student(
        request.form.get("id"), request.form.get("name"), request.form.get("gender"), request.form.get("age"),
        request.form.get("department"), request.form.get("major")
    )
    stu_pwd = model.StudentPassword.StudentPassword(student.student_id, request.form.get('pwd'))
    pwd: str = request.form.get("pwd")
    try:
        state_info = controller.AdminDao.add_student(student)  # State OK
        state_pwd = controller.AdminDao.add_student_password(stu_pwd)  # State OK
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILED


# TODO(接口：修改学生信息：完成)
@app.route('/editStudentInfo', methods=['post'])
def edit_student():
    # Get student form
    student = model.Student.Student(
        request.form.get("id"), request.form.get("name"), request.form.get("gender"), request.form.get("age"),
        request.form.get("department"), request.form.get("major")
    )
    state = controller.AdminDao.edit_student(student)
    return 'edit_student'


# TODO(接口：修改学生密码：完成)
@app.route('/editStudentPwd', methods=['post'])
def edit_student_pwd():
    aid = request.form.get('aid')
    stu_pwd = model.StudentPassword.StudentPassword(
        request.form.get("sid"), request.form.get('pwd')
    )
    state = controller.AdminDao.edit_student_pwd(aid, stu_pwd)
    return state


# TODO(接口：删除学生信息和密码：完成)
@app.route('/deleteStudent', methods=['post'])
def delete_student():
    sid = request.form.get('id')
    state_info = controller.AdminDao.delete_student_info_and_pwd(sid)
    return state_info


# TODO(接口：添加课程表：完成)
@app.route('/addCourse', methods=['post'])
def addCourse():
    course = model.Course.Course(
        request.form.get("cid"), request.form.get("cname"),
        request.form.get("credit"), request.form.get("time"),
        request.form.get("teacher"), request.form.get("title")
    )
    state = controller.AdminDao.add_course(course)
    return state


# TODO(接口：修改课程表：完成)
@app.route('/editCourse', methods=['post'])
def editCourse():
    course = model.Course.Course(
        request.form.get("cid"), request.form.get("cname"),
        request.form.get("credit"), request.form.get("time"),
        request.form.get("teacher"), request.form.get("title")
    )
    state = controller.AdminDao.edit_course(course)
    return state


# TODO(接口：删除课程表：完成)
@app.route('/deleteCourse', methods=['post'])
def deleteCourse():
    cid = request.form.get("cid")
    state = controller.AdminDao.delete_course(cid)
    return state


# TODO(接口：学生选课：完成)
@app.route('/confirmSelectCourse', methods=['post'])
def confirm_select_course():
    record = model.CourseRecord.CourseRecord(request.form.get("cid"), request.form.get("sid"), "null")
    state = controller.StudentDao.selectCourse(record)
    return state


# TODO(接口：删除选课记录：完成)
@app.route('/deleteCourseRecord', methods=['post'])
def delete_course_record():
    state = controller.AdminDao.delete_course_record(request.form.get("sid"), request.form.get("cid"))
    return state


# TODO(接口：修改管理员密码：完成)
def editAdminPassword():
    new_pwd = request.form.get("new_pwd")
    admin = model.Admin.Teacher(
        request.form.get("aid"), request.form.get("aname"), request.form.get("pwd")
    )
    state = controller.AdminDao.edit_admin_password(admin, new_pwd)
    return state


# TODO(接口：修改选课记录：待完善)
@app.route('/editCourseRecord', methods=['post'])
def editCourseRecord():
    course = model.CourseRecord.CourseRecord(
        request.form.get("cid"), request.form.get("cname"), request.form.get("score")
    )
    state = controller.AdminDao.edit_course_record(course)
    return state


# TODO(接口：获取课程表：待完善)
@app.route('/getCourse', methods=['post'])
def getCourse():
    state = controller.BasicDao.get_course()
    return state


# TODO(接口：添加管理员（不开放）：待完善)
@app.route('/addTeacher', methods=['post'])
def addAdmin():
    admin = model.Admin.Teacher(request.form.get("aid"), request.form.get("aname"), request.form.get("pwd"))
    state = controller.AdminDao.add_admin(admin)
    return state


if __name__ == '__main__':
    app.run()
