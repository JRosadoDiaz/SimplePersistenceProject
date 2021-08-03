from Employee import Employee

employees = [
    #Employee(101, "Jose", "Rosado", 1996)
]


def PrintPeopleDetails(filename):
    f = open(filename,"r")
    lines = f.readlines()
    for x in lines:
        emp = x.split(",")
        #print(emp)
        newEmployee = Employee(emp[0], emp[1], emp[2], emp[3])
        employees.append(newEmployee)

def PrintEmployees():
    for x in employees:
        print(x.get_employee_first_name(), x.get_employee_hire_year())
    