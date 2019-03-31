# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:39:38 2019

@author: Fanming
"""

class Person():
    firstName = ''
    lastName =''
    birthday =''
    
    def __init__(self,firstName='',lastName='',birthday=''):
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        
    def printPersonInformation(self):
        print(self.firstName,self.lastName,self.birthday)
        
    
class Student(Person):
    majorSubject = ''
    minorSubject = ''
    CourseList = []
    
    def __init__(self,firstName='',lastName='',birthday='',Major='MIS',Minor=''):
        super().__init__(firstName, lastName, birthday)
        self.majorSubject = Major
        
    def joinCourse(self,Course):
        self.CourseList.append(Course)
        
    def dropCourse(self,Course):
        self.CourseList.remove(Course)
#%%        
p1=Person('Fanming','Sun','19910917')
p1.printPersonInformation()

s1 = Student('Betty','Wang','10/28/2001')
s1.printPersonInformation()
#%%
s1.joinCourse('SoftwareEngineer')
s1.joinCourse('DataMining')
s1.joinCourse('AI')

print(s1.CourseList)
print(s1.majorSubject)
s1.dropCourse('AI')
print(s1.CourseList)

s2 =Student('Fanming','Sun','19910917')
print(s2.majorSubject)