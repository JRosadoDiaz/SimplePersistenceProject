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

def AddEmployee(filepath, id, firstName, lastName, hireDate):
    with open(filepath + "/" + id + ".txt", "w") as f:
        f.write(id + ", " + firstName.upper() + ", " + lastName.upper() + ", " + hireDate)

def DeleteEmployee(filepath, id):
    os.remove(filepath + "/" + id + ".txt")

def UpdateEmployee(filepath, id, firstName, lastName, hireDate):
    with open(filepath + "/" + id + ".txt", "w") as f:
        f.write(id + ", " + firstName.upper() + ", " + lastName.upper() + ", " + hireDate)

def read_files(filepath):
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        lines = f.readlines()
        for x in lines:
            emp = x.split(",")
            #print(emp)
            newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
            employees.append(newEmployee)

def check_id_exists(filepath, id):
    for file in os.listdir(filepath):
        thisNum = int(file.split(".")[0])
        if (id == thisNum):
            return True
    return False


