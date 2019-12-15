# coding:utf-8


# 定义一个日期类，打印出生日期
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def print_info(self):
        print("The birth is %s-%s-%s" % (self.year, self.month, self.day))


print("==================测试Date类=====================")
date = Date(year="2019", month="12", day="15")
date.print_info()


# 定义People类，有名字、年龄、出生的年/月、日，有走路的技能。
class People:
    def __init__(self, name, age, year, month, day):
        self.name = name
        self.age = age
        self.birthday = Date(year, month, day)

    def walk(self):
        print("%s is walking " % self.name)


print("==================测试People类=====================")
people = People(year="1988", month="11", day="20", name="张三", age=32)
people.birthday.print_info()


# 定义Teacher类，继承People类的特征和技能,并增加课程属性以及教书的技能
class Teacher(People):
    def __init__(self, name, age, year, month, day, course):
        People.__init__(self, name, age, year, month, day)
        self.course = course

    def teach(self):
        print("% s teaches %s" % (self.name, self.course))


print("==================测试Teacher类=====================")
teacher = Teacher(year="1988", month="11", day="20", name="Lucy", age=32, course="Python")
teacher.birthday.print_info()
teacher.walk()
teacher.teach()


# 定义Student类，继承People类的特征和技能,并增加学习组名属性以及学习的技能
class Student(People):
    def __init__(self, name, age, year, month, day, group):
        People.__init__(self, name, age, year, month, day)
        self.group = group

    def study(self):
        print("% s is studying  in   %s" % (self.name, self.group))


print("==================测试Student类=====================")
student = Student(year="1997", month="11", day="20", name="Jim", age=32, group="Group2")
student.birthday.print_info()
student.walk()
student.study()
