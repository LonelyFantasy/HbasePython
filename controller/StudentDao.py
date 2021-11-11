# -*- coding: utf-8 -*-
import model.CourseRecord
import server.HBaseConnect
import controller.BasicDao
import model.ReturnValue as Value

# Operate State
SUCCESS = Value.SUCCESS
FAILURE = Value.FAILURE
NO_DATA = Value.NO_DATA
EXIST = Value.EXIST
course_list = []


# TODO(学生选课：完成)
def selectCourse(record: model.CourseRecord.CourseRecord):
    connection = server.HBaseConnect.HBaseConnect()
    connection.start()
    try:
        table = connection.get_table('CourseRecord')
        new_row = record.course_id + record.student_id    # Create only row
        check_data = table.row(new_row)
        # print(str(check_data[new_row], encodings="utf-8"))
        if check_data:  # If student has already chosen the course, then
            return EXIST
        else:
            table.put(new_row, {'CourseID:': record.course_id, 'StudentID:': record.student_id, 'Score:': record.score})
        # print(str(check_data[new_row], encodings="utf-8"))
        connection.stop()
        return SUCCESS
    except Exception as e:
        print(e)
        return FAILURE
