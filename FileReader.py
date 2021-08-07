import os
import pickle
from Employee import Employee


employees = []
filepath = "./people/long"

# Not used yet
def change_file_path(path):
    filepath = path

def PrintPeopleDetails():
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        print("FILE: " + file)
        print(f.read())
        print()

def PrintEmployees():
    read_files(filepath)
    for x in employees:
        x.toString()

def AddEmployee(id, firstName, lastName, hireDate):
    f = open(filepath + "/" + id + ".txt", 'w')
    f.write(id + ", " + firstName.upper() + ", " + lastName.upper() + ", " + hireDate)
    f.close()

def UpdateEmployee(id, firstName, lastName, hireDate):
    f = open(filepath + id + ".txt", "w")
    f.write(id + ", " + firstName.upper() + ", " + lastName.upper() + ", " + hireDate)
    f.close()

def DeleteEmployee(id):
    os.remove(filepath + "/" + id + ".txt")

def SerializeAllEmployees():
    print("Serializing all employees...")
    # iterate through each file in people/long
    for file in os.listdir(filepath):
        newEmployee = None
        # read the file and generate an Employee object
        f = open(filepath + "/" + file, 'r')
        lines = f.readlines()
        for x in lines:
            emp = x.split(",")
            newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
        # Create the new serialized file
        serFilePath = filepath + " serialized/" + newEmployee.get_employee_id()
        fser = open(serFilePath + ".ser", 'ab')
        pickle.dump(newEmployee, fser)
        fser.close()

    print("Done!")

def FindEmployeeById(id):
    # go to serialized folder and iterate over each file
    for file in os.listdir(filepath + " serialized"):
        # once found, deserialize and return employee object to string
        if file == str(id) + ".ser":
            fileSer = open(filepath + " serialized/" + file, "rb")
            file = pickle.load(fileSer)
            print(file.toString())

def read_files():
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        lines = f.readlines()
        newEmployee = None
        for x in lines:
            emp = x.split(",")
            newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
        employees.append(newEmployee)

def FindEmployeeByLastName(lastName):
    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        lines = f.readlines()
        for x in lines:
            emp = x.split(", ")
            if(emp[2] == lastName):
                return Employee(emp[0], emp[1], emp[2], emp[3])
    return 0

def FindAllEmployeesByLastName(lastName):
    returnedEmployees = []

    for file in os.listdir(filepath):
        f = open(filepath + "/" + file, "r")
        lines = f.readlines()
        for x in lines:
            emp = x.split(", ")
            if(emp[2] == lastName):
                returnedEmployees.append(Employee(emp[0], emp[1], emp[2], emp[3]))
    return returnedEmployees

def check_id_exists(filepath, id):
    for file in os.listdir(filepath):
        thisNum = int(file.split(".")[0])
        if (id == thisNum):
            return True
    return False

def PrintSerializedDetails(path):
    print("hello")

def GetAllEmployees(EmployeeMap):
    print("Hello")

def PrintAllEmployees():
    print("Hello")

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
