from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from dateutil import parser
from dateutil.relativedelta import relativedelta


class Person(ABC):

    def __init__(self, surname, birthdate):
        self._surname = surname
        self._birthdate = birthdate
        self._age = self.get_age()

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_age(self):
        pass


class Enrollee(Person):

    def __init__(self, surname, birthdate, faculty):
        super().__init__(surname, birthdate)
        self._faculty = faculty

    def get_info(self):
        return self._surname, self._birthdate, self._faculty

    def get_age(self):
        current_date = datetime.now()
        birthdate = parser.parse(self._birthdate)
        age = relativedelta(current_date, birthdate)
        return age.years

    def __str__(self):
        res = (self._surname, self._birthdate, self.get_age(), self._faculty)
        return str(res)


class Student(Person):

    def __init__(self, surname, birthdate, faculty, year):
        super().__init__(surname, birthdate)
        self._faculty = faculty
        self._year = year

    def get_info(self):
        return self._surname, self._birthdate, self._faculty, self._year

    def get_age(self):
        current_date = datetime.now()
        birthdate = parser.parse(self._birthdate)
        age = relativedelta(current_date, birthdate)
        return age.years

    def __str__(self):
        res = (self._surname, self._birthdate, self.get_age(), self._faculty, self._year)
        return str(res)


class Teacher(Person):

    def __init__(self, surname, birthdate, duty, exp):
        super().__init__(surname, birthdate)
        self._duty = duty
        self._exp = exp

    def get_info(self):
        return self._surname, self._birthdate, self._duty, self._exp

    def get_age(self):
        current_date = datetime.now()
        birthdate = parser.parse(self._birthdate)
        age = relativedelta(current_date, birthdate)
        return age.years

    def __str__(self):
        res = (self._surname, self._birthdate, self.get_age(), self._duty, self._exp)
        return str(res)


list_of_persons = [Enrollee('Brown', '21-04-1996', 'Math'),
                   Student('Tven', '14-02-1999', 'Physics', 3),
                   Teacher('Black', '10-12-1980', 'IT', 15)]


def get_db(ls):
    for i in ls:
        print(i)


def get_in_range(start, end, ls):
    date_range = [i for i in range(start, end + 1)]

    def check_range(x):
        if x.get_age() in date_range:
            return True
        else:
            return False

    return filter(check_range, ls)


get_db(list_of_persons)

new_lst = get_in_range(21, 24, list_of_persons)

get_db(new_lst)
