import os
from Employee import Employee

employees = []

def PrintPeopleDetails(filepath):
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        print("FILE: " + file)
        print(f.read())
        print()

def PrintEmployees(filepath):
    read_files(filepath)
    for x in employees:
        x.toString()

def read_files(filepath):
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        lines = f.readlines()
        for x in lines:
            emp = x.split(",")
            #print(emp)
            newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
            employees.append(newEmployee)
