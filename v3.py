'''class properties
class Grader():
    REPRESENT GRADE IN NUMERIC SCORE
    def __init__(self,grade=0):
        self.grade=grade
math=Grader(90)
print('the math grade was %s' % math.grade)
math.grade=101
print('the math grade was %s' % math.grade)'''


class Grades():
    '''properties'''
    def __init__(self,score=0):
        self._score=score
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if value>100 or value<0:
            raise ValueError('Invalid Score')
        self._score=value

mathy=Grades(90)

print('the math grade was %s' % mathy.score)
try:
    mathy.score=100
except ValueError:
    print('not allowed')
    
    
class Ready():
    @property
    def constant(self):
        return 24
only=Ready()
print('%s has' %only.constant)
try:
    only.constant=25
except AttributeError:
    print('no change')







    
class 
