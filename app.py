import happybase
from flask import Flask, request, Response

import dao.AdminDao
import model.Student
import server.HBaseConnect
import model.StudentPassword
from dao.BasicDao import password_check

SUCCESS = "SUCCESS"
FAILED = "FAILED"

app = Flask(__name__)


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['post'])
def login():
    # Get login form
    userid = request.form.get("id")
    pwd = request.form.get("password")
    user_type = request.form.get("user_type")
    result = password_check(str(userid), pwd, int(user_type))
    return "data"


@app.route('/addStudent', methods=['post'])
def add_student():
    # Get student form
    student = model.Student.Student(
        request.form.get("id"), request.form.get("name"), request.form.get("gender"), request.form.get("age"),
        request.form.get("department"), request.form.get("major")
    )
    stu_pwd = model.StudentPassword.StudentPassword(
        student.student_id, request.form.get('pwd')
    )
    pwd: str = request.form.get("pwd")
    try:
        state_info = dao.AdminDao.add_student(student)  # State OK
        state_pwd = dao.AdminDao.add_student_password(stu_pwd)  # State OK
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILED


@app.route('/deleteStudent', methods=['post'])
def delete_student():
    # Get student form
    sid = request.form.get('id')
    state_info = dao.AdminDao.delete_student_info_and_pwd(sid)
    # state_pwd = dao.AdminDao.delete_pwd(sid)
    return state_info


if __name__ == '__main__':
    app.run()
