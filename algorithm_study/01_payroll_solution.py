# -*- coding: utf-8 -*-
"""
**Q1:** In this example we will try to make a small payroll. In other words, when the day worked and daily wages are entered on the keyboard, we will make the algorithm that calculates the net monthly wage to be received by that person according to the following rules .

Monthly gross income = daily wage * number of days worked
Income tax = monthly gross income * tax rate
Net monthly wage = Monthly gross income - Income tax

Rules:
* The number of working days should not be more than 31
* The income tax rate should be applied as 20% of the monthly gross income. However, it should be applied as 25% for those with a monthly income of more than 5000.
"""

def salary(working_day, daily_price):
  if working_day < 31:
    monthly_income = working_day * daily_price   
    if monthly_income > 5000:
      tax_rate = monthly_income / 4    
    else:
      tax_rate = monthly_income / 5       
    income_rate = monthly_income * tax_rate
    net_monthly_fee = monthly_income - income_rate
    return net_monthly_fee  
  else:
    working_day = working_day -31
    return salary(working_day, daily_price)
  
salary(30,50)
