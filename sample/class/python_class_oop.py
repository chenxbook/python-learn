# coding:utf-8
# 面向对象编程

# 定义一个Student类，这个类拥有name和score两个属性Property。


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        """打印一个学生的成绩"""
        print("%s: %s" % (self.name, self.score))


Tom = Student("Tom", 85)
Jim = Student("Jim", 100)
Tom.print_score()
Jim.print_score()
