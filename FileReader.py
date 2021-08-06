import os
import pickle
from Employee import Employee


employees = []

def PrintPeopleDetails():
    filepath = './people/long'
    for file in os.listdir("./Samples"):
        f = open("./Samples/" + file, "r")
        print("FILE: " + file)
        print(f.read())
        print()

def PrintEmployees():
    read_files('./people/long')
    for x in employees:
        x.toString()

def AddEmployee(id, firstName, lastName, hireDate):
    with open("./people/long" + id + ".txt", "w") as f:
        f.write(id + ", " + firstName.upper() + ", " + lastName.upper() + ", " + hireDate)

def DeleteEmployee(id):
    os.remove("./people/long/" + id + ".txt")

def UpdateEmployee(id, firstName, lastName, hireDate):
    with open("./people/long/" + id + ".txt", "w") as f:
        f.write(id + ", " + firstName.upper() + ", " + lastName.upper() + ", " + hireDate)

def read_files():
    filepath = './people/long'
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        lines = f.readlines()
        for x in lines:
            emp = x.split(",")
            newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
            employees.append(newEmployee)

def check_id_exists(filepath, id):
    for file in os.listdir(filepath):
        thisNum = int(file.split(".")[0])
        if (id == thisNum):
            return True
    return False

def SerializeAllEmployees(path, serPath):
    print("Serializing all employees...")

