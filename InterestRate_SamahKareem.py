

LoanAmount = eval(input("Loan Amount: "))
Years = eval(input("Number of Years: "))
print("Interest rate\tMonthly Payment\tTotalPayment")
annualInterestRate = 5.0
while annualInterestRate <= 8.0:
    MIR = annualInterestRate/1200
    MP = (LoanAmount * MIR)/(1- 1/((1+MIR)**(Years*12)))
    totalPayment = MP*Years*12
    print("%.3f%%\t\t\t%.2f\t\t\t%.2f" % (annualInterestRate, MP, totalPayment))
    annualInterestRate = (annualInterestRate+ (1.0/8.0))