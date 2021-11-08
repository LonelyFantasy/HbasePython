# -*- coding: utf-8 -*-
import server.HBaseConnect


def password_check(user_id: str, password: str, user_type: int):
    if user_type == 1:  # Student Password
        # Scan to table: StudentPassword.
        connection = server.HBaseConnect.HBaseConnect()
        pwd_table = connection.get_table("StudentPassword")
        try:
            pwd_table.row(user_id)
            print(pwd_table)
        except Exception as e:
            print(e.args[0])
            return e

