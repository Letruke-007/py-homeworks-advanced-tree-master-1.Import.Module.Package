from application import salary
from application.db import people
from datetime import date
from progress import bar
if __name__ == '__main__':
    print(date.today())
    salary.calculate_salary()
    people.get_employees()
