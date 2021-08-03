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
            print('1 selected')
            FileReader.PrintPeopleDetails(path)
        elif sel == '2':
            print('2 selected')
            FileReader.PrintEmployees(path)
        elif sel == '0':
            print('Closing program.')
        else:
            print('Instructions unclear.')



if __name__ == "__main__":
    main()