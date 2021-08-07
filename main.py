#imports
import FileReader

#main method
def main():
    display_interface()

def display_interface():
    # path = input('Please enter path to files:\n')
    # FileReader.change_file_path(path)

    sel = ''
    while sel != '0':
        # print('1 - View file contents')
        # print('2 - View employees from files')
        # print('3 - Add Employee')
        # print('4 - Delete Employee')
        # print('5 - Update Employee')
        print('1 - Serialize Employees')
        # print('2 - View Employee by ID')
        print('2 - Find Employee by ID')
        print('3 - Find Employees by Last Name')
        print('0 - Exit')

        sel = input('Select an option: ')
        # if sel == '1':
        #     print('Viewing file information:\n')
        #     FileReader.PrintPeopleDetails()
        # elif sel == '2':
        #     print('Viewing employee data:\n')
        #     FileReader.PrintEmployees()
        # elif sel == '3':
        #     add_employee()
        # elif sel == '4':
        #     delete_employee()
        # elif sel == '5':
        #     update_employee()
        if sel == '1':
            FileReader.SerializeAllEmployees()
        elif sel == '2':
            find_employee_by_id()
        elif sel == '3':
            find_by_last_name()
        elif sel == '0':
            print('Closing program.')
        else:
            print('Instructions unclear.')

def view_selected_employee():
    idExists = False
    selectedId = 0
    while idExists == False:
        selectedId = input('Enter ID to view or 0 to exit: ')
        idExists = FileReader.check_id_exists('./people/long serialized', int(selectedId))
        if (selectedId == '0'):
            idExists = True
        if (idExists == False):
            print('Failed to find ID, try another.')
    
    if(selectedId == '0'):
        return
    else:
        FileReader.GetSerializedEmployee(int(selectedId))

def find_employee_by_id():
    idExists = False
    selectedId = 0
    while idExists == False:
        selectedId = input('\nEnter ID to view or 0 to exit: ')
        idExists = FileReader.check_id_exists('./people/long serialized', int(selectedId))
        if (selectedId == '0'):
            idExists = True
        if (idExists == False):
            print('Failed to find ID, try another or try serializing first.')
    
    if(selectedId == '0'):
        return
    else:
        FileReader.FindEmployeeById(int(selectedId))

def find_by_last_name():
    lastName = input("\nEnter last name to search for: ")
    sel = input("1 for the first employee, 2 for all employees: ")
    if (sel == '1'):
        employee = FileReader.FindEmployeeByLastName(lastName.upper())
        if (employee == 0):
            print('No matching employee found.')
        else:
            print(employee.toString())
    elif (sel == '2'):
        employees = FileReader.FindAllEmployeesByLastName(lastName.upper())
        if (len(employees) == 0):
            print('No matching employees found.')
        else:
            for employee in employees:
                print(employee.toString())
    else:
        print("Couldn't understand the request.")

if __name__ == "__main__":
    main()

# def add_employee():
#     idExists = True
#     selectedId = 0
#     while idExists == True:
#         selectedId = input('Enter ID to add or 0 to exit: ')
#         if (selectedId == '0'):
#             idExists = True
#         idExists = FileReader.check_id_exists('./people/long', int(selectedId))
#         if (idExists == True):
#             print('ID already exists, try another.')
    
#     if (selectedId == '0'):
#             return
#     firstName = input('Please enter the first name to add:\n')
#     lastName = input('Please enter the last name to add:\n')
#     hireDate = input('Please enter the hire year:\n')
#     FileReader.AddEmployee(selectedId, firstName, lastName, hireDate)

# def update_employee():
#     idExists = False
#     selectedId = 0
#     while idExists == False:
#         selectedId = input('Enter ID to update or 0 to exit: ')
#         idExists = FileReader.check_id_exists('./people/long', int(selectedId))
#         if (selectedId == '0'):
#             idExists = True
#         if (idExists == False):
#             print('Failed to find ID, try another.')
    
#     if (selectedId == '0'):
#             return
#     firstName = input('Please enter updated first name:\n')
#     lastName = input('Please enter updated last name:\n')
#     hireDate = input('Please enter updated hire date:\n')
#     FileReader.UpdateEmployee(selectedId, firstName, lastName, hireDate)

# def delete_employee():
#     idExists = False
#     selectedId = 0
#     while idExists == False:
#         selectedId = input('Enter ID to delete or 0 to exit: ')
#         if (selectedId == '0'):
#             idExists = True
#         idExists = FileReader.check_id_exists('./people/long', int(selectedId))
#         if (idExists == False):
#             print('Failed to find ID, try another.')
    
#     if(selectedId == '0'):
#         return
#     else:
#         FileReader.DeleteEmployee(selectedId)