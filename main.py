path = input('Please enter path to files:\n')

sel = ''
while sel != '0':
    print('\n1 - View file contents')
    print('2 - View employees from files')
    print('0 - Exit')

    sel = input('Select an option: ')
    if sel == '1':
        print('1 selected')
        # print_people_details(path)
    elif sel == '2':
        print('2 selected')
        # print_employees(path)
    elif sel == '0':
        print('Closing program.')
    else:
        print('Instructions unclear.')
#imports
import FileReader

#main method
def main():
    print("Hello world")
    #FileReader.PrintPeopleDetails("test.txt")
    #FileReader.PrintEmployees()


if __name__ == "__main__":
    main()