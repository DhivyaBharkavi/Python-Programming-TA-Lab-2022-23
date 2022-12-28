basic_pay=eval(input("Enter your salary "))
da=(88%100)*basic_pay
hra=(8%100)*basic_pay
cca=1000
insurance=2000
pf=(10%100)*basic_pay
gross_pay=basic_pay+da+hra+cca
deductions=insurance+pf
salary=basic_pay+gross_pay+deductions
print("Acutal salary is ",salary)
