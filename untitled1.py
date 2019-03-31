# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:08:03 2019

@author: Fanming
"""

class   Person():
    firstName = ''
    lastName = ''
    birthday = ''
    
    def __init__(self,firstName,lastName,birthday):
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
    
    def printPersonalInformation(self):
        print(self.firstName,self.lastName,self.birthday)
        
    
class Student(Person):
    majorSubject = ''
    minorSubject =''
    CourseList = []
    
    def __init__(self, firstName,lastName,birthday,Major,Minor):
        super().__init__(firstName, lastName, birthday)
        self.majorSubject= Major
        self.minorSubject= Minor
    
    def joinCourse(self,Course):
        self.courseList.append(Course)
    def dropCourse(self,Course):
        self.CourseList.remove(Course)
    def printPersonalInformation(self):
        print(self.firstName,self.lastName,self.birthday,self.majorSubject,self.minorSubject)
#%%
p1 = Person('Amy','Chang','10/20/2001')
p1.printPersonalInformation() 
#%%
s1 = Student('Betty','Wang','10/28/2001')
s1.printPersonalInformation()
#%%
