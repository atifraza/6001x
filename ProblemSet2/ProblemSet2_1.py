balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
# Working Code below
totalPaid = 0
for month in range(12):
    minMonthlyPayment = round( monthlyPaymentRate * balance, 2 )
    totalPaid += minMonthlyPayment
    unpaidBalance = balance - minMonthlyPayment
    balance = unpaidBalance + round( unpaidBalance * annualInterestRate/12.0, 2 )
    print('Month: ' + str(month+1))
    print('Minimum monthly payment: ' + str(minMonthlyPayment) )
    print('Remaining balance: ' + str(balance) )
    
print('Total paid: ' + str(totalPaid))
print('Remaining balance: ' + str(balance) )