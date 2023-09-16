import string

from _decimal import Decimal

from BusinessObj.Charateristics import Characteristics


class Person:
    name: string;
    age: int;
    occupation: string;
    salary: Decimal;
    characteristic: Characteristics;

    def __init__(self, name, age, occupation, salary, character):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.salary = salary
        self.characteristic = character

    def name(self):
        return self.name

    def age(self):
        return  self.age

    def occupation(self):
        return  self.occupation

    def salary(self):
        return self.salary

    def characteristic(self):
        return self.characteristic




