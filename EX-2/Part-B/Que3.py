"""
An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay.
Overtime pay equals the total overtime hours multiplied by 1.5 times the hourly wage.
Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and displays an employee’s total weekly pay.
"""
hourly_wage = float(input("Enter employees hourly wage "))
regular_hours = float(input("Enter employees regular hours "))
overtime_hours = float(input("Enter employees overtime hours "))
overtime_pay = overtime_hours * 1.5 * hourly_wage
total_weekly = hourly_wage * regular_hours+overtime_pay
print("The employee's total weekly pay is ",total_weekly)
