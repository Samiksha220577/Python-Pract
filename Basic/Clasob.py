# class student:
#     def __init__ (self,name,roll,age):
#         self.name = name
#         self.roll = roll
#         self.age = age
#
#     def display(self):
#         print("name:{}".format(self.name))
#         print("roll:{}".format(self.roll))
#         print("age:{}".format(self.age))
#
# s1 = student("sami",22,17)
# s1.display()


# _______________________________________________________________

from abc import ABC


class polygon(ABC):
    def sides(self):
        pass


class triangle(polygon):
    def sides(self):
        print("three sides")


class square(polygon):
    def sides(self):
        print("four sides")


class circle(polygon):
    def sides(self):
        print("no sides")


t = triangle()
t.sides()
s = square()
s.sides()
c = circle()
c.sides()

