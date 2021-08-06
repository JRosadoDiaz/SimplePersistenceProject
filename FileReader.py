import os
import pickle
from Employee import Employee


employees = []
filepath = "./people/long/"

def PrintPeopleDetails():
    for file in os.listdir(filepath):
        f = open(filepath + file, "r")
        print("FILE: " + file)
        print(f.read())
        print()

def PrintEmployees():
    read_files(filepath)
    for x in employees:
        x.toString()

def AddEmployee(id, firstName, lastName, hireDate):
    #create a file
    f = open(filepath + id + ".txt", 'w')

    #write parameter values to file
    f.write(id + "," + firstName + "," + lastName + "," + hireDate)

    #close file
    f.close()

def UpdateEmployee(id, firstName, lastName, hireDate):
    #locate file with id
    f = open(filepath + "/" + id + ".txt", "w")

    #rewrite contents of file
    f.write(id + "," + firstName + "," + lastName + "," + hireDate)

    #close file
    f.close()

def DeleteEmployees(id):
    os.remove(filepath + "/" + id + ".txt")

def SerializeAllEmployees(path, serPath):
    print("Serializing all employees...")
    # iterate through each file in people/long
    for file in os.listdir(filepath):
        serFile = open(filepath + "/" + file, "ab") # ab = appending in binary format
        # use the pickle library to serlialize each file into 'people/long serialized'
        pickle.dump(serFile, filepath + " serialized")
        serFile.close()

def GetSerializedEmployee(id):
    # go to serialized folder and 

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




# def get_next_id(filepath):
#     thisNum = 0
#     lastNum = 0

    # doesn't work with default ascii sorting.

    # for file in os.listdir(filepath):
        # thisNum = int(file.split(".")[0])
        # print(int(file.split('.')[0]))
        # if (thisNum - 1 != lastNum):
        #     return thisNum - 1
        # lastNum = thisNum
    #return thisNum + 1
