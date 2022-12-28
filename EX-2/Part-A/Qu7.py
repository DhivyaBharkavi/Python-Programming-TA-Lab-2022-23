principal=eval(input("Enter your principal amount "))
interest_rate=eval(input("Enter your rate value "))
time_in_years=eval(input("Enter your time "))
simple_interest_formula1=(principal*interest_rate*time_in_years)/100
print("Forumula 1 for Simple interest is ",simple_interest_formula1)
simple_interest_formula2=principal*(1+(interest_rate*time_in_years))
print("Forumula 2 for Simple interest is ",simple_interest_formula2)

