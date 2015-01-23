balance = 482443
annualInterestRate = 0.18
# Working Code below
monthlyInterestRate = annualInterestRate/12.0
originalBalance = balance
lowerLim = balance/12.0
upperLim = (balance *  pow(1+monthlyInterestRate, 12) )/12.0
fixedMonthlyPayment = (lowerLim+upperLim)/2
month = 0
while(month<12):
    unpaidBalance = balance - fixedMonthlyPayment
    balance = unpaidBalance + unpaidBalance*monthlyInterestRate
    if(month == 11 and abs(balance)>0.1 ):
        balance = originalBalance
        if(unpaidBalance<0):
            upperLim = fixedMonthlyPayment
        else:
            lowerLim = fixedMonthlyPayment
        fixedMonthlyPayment = (lowerLim+upperLim)/2
        month = 0
    else:
        month += 1
    
print('Lowest payment: ' + str(round(fixedMonthlyPayment, 2)) )