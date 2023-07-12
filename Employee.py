class Employee:

    # init method acts as a constructor
    def __init__(self, name, age, salary , gender ):

        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of the Employee is : ",self.name)
        print("Age of Employee is :" ,self.age)
        print("Salary of Employee is :",self.salary)
        print("Gender of the employee:",self.gender)

e = Employee('Chinmai Sutar',37,95000,'Female')
             
e.employee_details()   

