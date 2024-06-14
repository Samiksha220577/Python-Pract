# class vehicle:
#     def __init__(self,Vname,vColor):
#         self.name=Vname
#         self.color=vColor
#         print("constructor method is called")
#
#     def __del__(self):
#         print("destructor method is called")
#     def display(self):
#         print(f"my vehicle is {self.name} and my color is {self.color}")
# s=vehicle("Sam","red")
# # del s
# s.display()
# --------------------------------------------
# single inheritance
class Parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"the addition of a,b is :")
class child(Parent):
    def multiply(self):
        print(f"the multiplication of 5 , 6 is:")
c=child(1,5)
c.add()