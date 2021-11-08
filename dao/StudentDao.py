# -*- coding: utf-8 -*-
import thrift
import happybase

import server.HBaseConnect
from server.HBaseConnect import HBaseConnect

course_list = []


class StudentDao:
    def __init__(self, connection: HBaseConnect):
        self.connection = connection

    def select_course(self):
        # Get Course Data From HBase
        pass


def edit_info():
    pass


def edit_password():
    pass


def look_info():
    connection = server.HBaseConnect.HBaseConnect()
    table = connection.connection.table("student", use_prefix=True)
    table.row()


def look_course():
    pass


def out_course():
    pass


def check_profile():
    pass
