import application.salary as salary
import application.db.people as people
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now())
    print(salary.calculate_salary())
    print(people.get_employees())