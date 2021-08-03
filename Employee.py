class Employee:
    #Constructor
    def __init__(self, employee_id, first_name, last_name, hire_year):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.hire_year = hire_year.replace("\n", "")
    
    def get_employee_id(self):
        return self.employee_id

    def get_employee_first_name(self):
        return self.first_name

    def get_employee_last_name(self):
        return self.last_name

    def get_employee_hire_year(self):
        return self.hire_year

    def set_employee_id(self, id):
        self.employee_id = id

    def set_employee_first_name(self, name):
        self.first_name = name

    def set_employee_last_name(self, name):
        self.last_name = name

    def set_employee_hire_year(self, year):
        self.hire_year = year

    def toString(self):
            print("ID: " + self.get_employee_id() + ", Name: " + self.get_employee_first_name() + " " + self.get_employee_last_name() + ", Hire Year: " + self.get_employee_hire_year())    
