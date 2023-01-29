import Question10a as q10a

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time period: "))
print("Compound interest is: ", q10a.compound_interest(principal, rate, time))