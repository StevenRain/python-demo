class Human(object):
    def __init__(self, name):
        self.name = name


class Student(Human):
    def __init__(self, name, score):
        super(Student, self).__init__(name)
        # Human.__init__(self, name)
        self.score = score

    # This is a private method
    def _print_name(self):
        print(self.name)

    def print_score(self):
        print('name : %s, score : %s' % (self.name, self.score))


# print an object
def print_student(student):
    print('%s %s' % (student.name, student.score))


Steven = Student('Steven', 98)
Anna = Student('Anna', 88)
Steven.print_score()
Anna.print_score()
print_student(Anna)




class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


steven = Student()
steven.score = 100
steven.birth = 1992
print(steven.score)
print(steven.age)
