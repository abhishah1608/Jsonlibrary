# This is a sample Python script.
import jsonutility
from BusinessObj.Charateristics import Characteristics
from BusinessObj.Person import Person
import numpy

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    character = Characteristics('Male',28)
    p = Person(name='Abhi', age=28, occupation='Software Developer', salary = 75000, character= character)
    str = jsonutility.convertObjToJson(p)
    print(str)
    p1 = jsonutility.convertJsonToObj(str)
    print(p1['characteristic']['gender'])
    x = []
    x.append(p)
    x.append(p)
    print(jsonutility.convertObjToJson(x))



