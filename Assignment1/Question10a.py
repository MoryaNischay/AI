#function takes principal, rate and time as input and returns the compound interest
def compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time))