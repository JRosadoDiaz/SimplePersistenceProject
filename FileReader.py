from Employee import Employee

employees = []

def PrintPeopleDetails(filename):
    f = open(filename, "r")
    print(f.read())

def PrintEmployees(filename):
    read_file(filename)
    for x in employees:
        print("ID: " + x.get_employee_id() + ", Name: " + x.get_employee_first_name() + " " + x.get_employee_last_name() + ", Hire Year: " + x.get_employee_hire_year())    

def read_file(filename):
    f = open(filename,"r")
    lines = f.readlines()
    for x in lines:
        emp = x.split(",")
        #print(emp)
        newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
        employees.append(newEmployee)
