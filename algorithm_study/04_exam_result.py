# -*- coding: utf-8 -*-
"""

**Q4:** The algorithm that determines the conditions under which the student applying for a master's degree will be accepted and under which conditions will not be accepted has been coded.

Conditions:

* The student must have taken the GMAT exam and got at least 60 points

* If the applied department is engineering, it must have at least 60 points from the TOEFL or IELTS exam.


* If these conditions are met, at least 60 points from the entrance exam of the university
"""

department = input("What is your department ? ")

def exams(gmat, toefl, ielts, y):
    
  if gmat >= 60:
    
    if department == "engineering":
        
      if toefl >= 60 or ielts >= 60:
        return üni_exam(y)
    
      else:
        print("Your application has been denied.")
        
    else:
      return üni_exam(y)  

  else:
    print("Your application has been denied.")

def üni_exam(y):
    
  if y >= 60:
    print("Your application has been accepted")
    
  else:
        print("Your application has been denied.")

exams(84,86,74,95)
