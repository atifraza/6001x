balance = 4773
annualInterestRate = 0.2
# Working Code below
originalBalance = balance
monthlyInterestRate = annualInterestRate/12.0
fixedMonthlyPayment = 10
month = 0
while(month<12):
    unpaidBalance = balance - fixedMonthlyPayment
    balance = unpaidBalance + unpaidBalance*monthlyInterestRate
    if(month == 11 and balance>0):
        balance = originalBalance
        fixedMonthlyPayment += 10
        month = 0
    else:
        month += 1
    
print('Lowest payment: ' + str(fixedMonthlyPayment) )