class vehicle:
    def __init__(self,Vname,vColor):
        self.name=Vname
        self.color=vColor
        print("constructor method is called")

    def __del__(self):
        print("destructor method is called")
    def display(self):
        print(f"my vehicle is {self.name} and my color is {self.color}")
s=vehicle("Sam","red")
# del s
s.display()
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
# ---------------------------------------------

file=open("Lmao.txt", "a")
data="Heheheh"
file.writelines(data)
file.close()
# -----------------------------
import json

file= open("file1.jason",'w')
data={
    "name" : "sami",
    "age":"18"

}
json.dump(data,file,indent=4)
file.close()
# -----------------------------
import csv
file=open("data.csv","r")
# file.close()
readerobj = csv.reader(file)
print(readerobj)
for row in readerobj:
    print(row)
file.close()
# -----------------------------
import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

# name of csv file
filename = "university_records.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)
# -------------------------------------
import csv
file=open("sample.csv","w")
writerobj=csv.writer(file)
headder=["name","age"]
body=[
    ["sami","18"],
    ["rishika","13"]

]
writerobj.writerow(headder)
writerobj.writerows(body)
file.close()
# ---------------------------
# filter
def verify(age):
    return age>18
data=[23,41,14,13,35]
print(list(filter(verify,data)))
# ---------------------------------------------
from functools import reduce
# reduce has to be imported from functools
def perform(a,b):
    return a*b
data=[1,2,3,4,5]
res = reduce(perform,data)
print(res)

# --------------------------------------------
from functools import reduce
data=[1,2,3,4,5]
res=reduce(lambda a,b:a*b,data)
print(res)
# --------------------------------------------
arr=[[2,5,4],
     [1,2,5],
     [4,6,2]]

arr.sort(key=lambda row:row[-1])
print(*arr,sep="\n")
# ------------------------------------------

