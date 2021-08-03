#imports
import FileReader

#main method
def main():
    display_interface()
    #FileReader.PrintPeopleDetails("test.txt")
    #FileReader.PrintEmployees()

def display_interface():
    path = input('Please enter path to files:\n')

    sel = ''
    while sel != '0':
        print('\n1 - View file contents')
        print('2 - View employees from files')
        print('0 - Exit')

        sel = input('Select an option: ')
        if sel == '1':
            print('Viewing file information:\n')
            FileReader.PrintPeopleDetails(path)
        elif sel == '2':
            print('Viewing employee data:\n')
            FileReader.PrintEmployees(path)
        elif sel == '0':
            print('Closing program.')
        else:
            print('Instructions unclear.')



if __name__ == "__main__":
    main()