"""
Responsibility 1: Handle employee details.
Responsibility 2: Calculate employee salary.
Responsibility 3: Generate employee reports.
"""
from random import randint

#Handle employee details.
class Employee:
    def __init__(self, name, salary, position):
        self.id = randint(10, 20)
        self.emp_name = name
        self.emp_salary = salary
        self.emp_position = position

#Calculate employee salary.
class SalaryCalculator:
    @staticmethod
    def salary_calculate(emp, bonus):
        post_bonus = emp.emp_salary + bonus
        return post_bonus

#Generate employee reports
class EmployeeReport:
    @staticmethod
    def generate_report(emp_list):
        print("{0} Employees Report {0}".format("#"*10))
        for emp in emp_list:
            print(f"Name : {emp.emp_name} || Position : {emp.emp_position} || Salary : {emp.emp_salary}")
        print("{0} Employees Report completed {0}".format("#" * 10))

if __name__ == "__main__":
    emp1 = Employee("Ram", 120000,"Senior S/w Eng")
    emp2 = Employee("shyam", 100000, "S/w Eng")
    emp3 = Employee("shima", 50000, "HR")

    EmployeeReport.generate_report([emp1, emp2, emp3])

    print(f"Bonus Calculator")
    bonus = SalaryCalculator.salary_calculate(emp1, 20000)
    print(f"Salary for emp {emp1.emp_name} post bonus is {bonus}")
    bonus = SalaryCalculator.salary_calculate(emp2, 2000)
    print(f"Salary for emp {emp2.emp_name} post bonus is {bonus}")