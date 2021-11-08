- 创建学生表
```shell
create 'Student', 'SInfo:StudentID', 'SInfo:SName', 'SInfo:SGender', 'SInfo:SAge', 'Studies:SDepartment', 'Studies:SMajor'
create 'Student', 'SInfo', 'Studies'
```

- 创建课程表

```shell
create 'Course', 'CInfo:CourseID', 'CInfo:CName', 'CInfo:Credit', 'CInfo:Time', 'Teaching:Teacher', 'Teaching:Title'
create 'Course', 'CInfo', 'Teaching'
```

- 创建选课记录表

```shell
create 'CourseRecord', 'CourseID', 'StudentID', 'Score'
```

- 创建管理员信息表
```shell
create 'Admin', 'AdminID', 'AdminName', 'Password'
```

- 创建学生密码表
```shell
create 'StudentPassword', 'StudentID', 'Password'
create 'studentpassword', 'StudentID', 'Password'
```