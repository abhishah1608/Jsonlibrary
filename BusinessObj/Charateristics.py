import string


class Characteristics:

    gender : string
    experience : int

    def __init__(self, gender, experience):
        self.gender = gender
        self.experience = experience

    def gender(self):
        return  self.gender

    def experience(self):
        return  self.experience
