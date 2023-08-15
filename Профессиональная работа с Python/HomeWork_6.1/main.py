from application.salary import calculate_salary  as cs
from application.db.people import get_employees as ge
from datetime import datetime
import GoogleTable


def todaydate():
    print(f'Сегодня {datetime.today().strftime("%d.%m.%Y")}')

if __name__ == '__main__':
    todaydate()
    cs()
    ge()