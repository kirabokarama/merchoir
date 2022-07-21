class Employee:
    # class variables
    id = None

    # instance variables
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        self.__salary = None


    # instance Methods
    def testing_stuff(self, message):
        return message
    
    # class method
    def testing_one():
        return "class Method"

    # static method
    @staticmethod
    def testing_two():
        return "static method"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

employee_one = Employee("James", "Kabera")
employee_one.id = 1

# employee_one.testing_stuff()

# print(employee_one.testing_stuff("instance method"))

# print(Employee.testing_two())


class DailyEmployee(Employee):
    def __init__(self, fname, lname, rate ):
        super().__init__(fname, lname)
        self.hourly_rate = rate

    def calculate_daily_pay(self, hours):
        return self.hourly_rate * hours

    def __str__(self) -> str:
        return "Daily Employee"




daily_emp = DailyEmployee("James", "Kabera", 1000)
# print(daily_emp.testing_stuff("child class"))
print(daily_emp)

'''' OOP pillars'''

# Encaspulation, inheritance, abstraction, polymorphism



