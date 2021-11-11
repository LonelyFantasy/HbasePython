# -*- coding: utf-8 -*-
import server.HBaseConnect
import model.ReturnValue as Value

# Operate State
SUCCESS = Value.SUCCESS
FAILED = Value.FAILURE
INFO_ERROR = Value.INFO_ERROR


# TODO(登录检查：待完善)
def login_check(user_id: str, password: str, user_type: int):
    print("user_type: " + str(user_type))
    if user_type == 1:  # Student Password
        # Scan to table: StudentPassword.
        connection = server.HBaseConnect.HBaseConnect()
        connection.start()
        pwd_table = connection.get_table("StudentPassword")
        try:
            get_data = pwd_table.row(user_id)
            print(str(get_data[b'Password:'], encoding="utf-8"))
            get_pwd = str(get_data[b'Password:'], encoding="utf-8")
            print(get_pwd)
            if password is get_pwd:
                return SUCCESS
            else:
                return INFO_ERROR
        except Exception as e:
            print(e)
            return e
    elif user_type == 2:  # Admin Password
        # Scan to table: Admin.
        connection = server.HBaseConnect.HBaseConnect()
        connection.start()
        pwd_table = connection.get_table("Admin")
        try:
            get_data = pwd_table.row(user_id)
            print(str(get_data[b'Password:'], encoding="utf-8"))
            get_pwd = str(get_data[b'Password:'], encoding="utf-8")
            print(get_pwd)
            if password is get_pwd:
                return SUCCESS
            else:
                return INFO_ERROR
        except Exception as e:
            print(e)
            return e


# TODO(获取课程表：待完善)
def get_course():
    connection = server.HBaseConnect.HBaseConnect()
    result_course_dict = connection.get_double_table_dict('Course')
    return result_course_dict


# TODO(查找学生：待完善)
def find_student(sid):
    connection = server.HBaseConnect.HBaseConnect()
    try:
        connection.start()
        table = connection.get_table("Student")
        id_key = "b'" + sid + "'"
        print(id_key)
        row = table.row(id_key)
        return "test"
    except Exception as e:
        print(e)
        return FAILED
