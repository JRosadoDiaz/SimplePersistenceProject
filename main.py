#imports
import FileReader

#main method
def main():
    display_interface()

def display_interface():
    path = input('Please enter path to files:\n')

    sel = ''
    while sel != '0':
        print('\n1 - View file contents')
        print('2 - View employees from files')
        print('3 - Add Employee')
        print('4 - Delete Employee')
        print('5 - Update Employee')
        print('6 - Serialize Employees')
        print('7 - View Employee by ID')
        print('0 - Exit')

        sel = input('Select an option: ')
        if sel == '1':
            print('Viewing file information:\n')
            FileReader.PrintPeopleDetails(path)
        elif sel == '2':
            print('Viewing employee data:\n')
            FileReader.PrintEmployees(path)
        elif sel == '3':
            add_employee(path)
        elif sel == '4':
            delete_employee(path)
        elif sel == '5':
            update_employee(path)
        elif sel == '6':
            serPath = input('Enter path to serialize files to:\n')
            FileReader.SerializeAllEmployees(path, serPath)
        elif sel == '7':
            view_selected_employee(path)
        elif sel == '0':
            print('Closing program.')
        else:
            print('Instructions unclear.')

def add_employee(path):
    firstName = input('Please enter the first name to add:\n')
    lastName = input('Please enter the last name to add:\n')
    hireDate = input('Please enter the hire year:\n')
    # print(FileReader.get_next_id(path)+1, firstName, lastName, hireDate)
    # FileReader.AddEmployee(FileReader.get_next_id(path)+1, firstName, lastName, hireDate)

def update_employee(path):
    idExists = False
    selectedId = 0
    while idExists == False:
        selectedId = input('Enter ID to update or 0 to exit: ')
        if (selectedId == '0'):
            idExists = True
        idExists = FileReader.check_id_exists(path, int(selectedId))
        if (idExists == False):
            print('Failed to find ID, try another.')
    
    if (selectedId == '0'):
            return
    firstName = input('Please enter updated first name:\n')
    lastName = input('Please enter updated last name:\n')
    hireDate = input('Please enter updated hire date:\n')
    # FileReader.UpdateEmployee(int(selectedId), firstName, lastName, hireDate)

def delete_employee(path):
    idExists = False
    selectedId = 0
    while idExists == False:
        selectedId = input('Enter ID to delete or 0 to exit: ')
        if (selectedId == '0'):
            idExists = True
        idExists = FileReader.check_id_exists(path, int(selectedId))
        if (idExists == False):
            print('Failed to find ID, try another.')
    
    if(selectedId == '0'):
        return
    else:
        x = 1
        # FileReader.DeleteEmployee(int(selectedId))

def view_selected_employee(path):
    idExists = False
    selectedId = 0
    while idExists == False:
        selectedId = input('Enter ID to delete or 0 to exit: ')
        if (selectedId == '0'):
            idExists = True
        idExists = FileReader.check_id_exists(path, int(selectedId))
        if (idExists == False):
            print('Failed to find ID, try another.')
    
    if(selectedId == '0'):
        return
    else:
        x = 1
        # FileReader.GetSerializedEmployee(int(selectedId))

if __name__ == "__main__":
    main()