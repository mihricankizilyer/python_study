# -*- coding: utf-8 -*-
"""**Q2**"""

def math(mid1, mid2, final, project):
  score = mid1*0.1+ mid2*0.1+ final*0.6+ project*0.2
  if 0<mid1<100 and 0<mid2<100 and 0<final<100 and 0<project<100:
    if score <=100 and score >85:
      return "A"
    elif score <=85 and score >70:
      return "B"
    elif score <=70 and score >55: 
      return "C"
    elif score <=55 and score >45:
      return "D"
    elif score <=45 and score >25:
      return "E"
    elif score <=25 and score >0:
      return "F"
def physic(mid1, mid2, final, project):
  score = mid1*0.1+ mid2*0.1+ final*0.6+ project*0.2
  if 0<mid1<100 and 0<mid2<100 and 0<final<100 and 0<project<100:
    if score <=100 and score >85:
      return "A"
    elif score <=85 and score >70:
      return "B"
    elif score <=70 and score >55: 
      return "C"
    elif score <=55 and score >45:
      return "D"
    elif score <=45 and score >25:
      return "E"
    elif score <=25 and score >0:
      return "F"
lesson1 = math(100,32,55,11) 
lesson2 = physic(98,76,85,92)
print("Letter grade in Math: {}".format(lesson1))
print("Letter grade in Physic: {}".format(lesson2))
