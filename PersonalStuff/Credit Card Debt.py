def Fix_credit_payment(balance, annualInterestRate, months):
    """
    Generates the fix amount of monthly payment needed to payoff the debt in given number of months
    requires:
        - Total Debt Balance,
        - Annual Interest Rates in percentage,
        - Number of Months

    """
    mem = balance
    upper = (balance + balance * annualInterestRate) / months
    lower = balance / months

    while True :
        fixed = (upper + lower) / 2
        for month in range(months):
            balance -= fixed
            balance += (annualInterestRate / months) * balance

        if round(balance, 1) > 0:
            balance = mem
            lower = fixed + 0.1
        elif round(balance, 1) < 0:
            balance = mem
            upper = fixed - 0.1
        else:
            print (f"Lowest fix payment: {round(fixed, 2):,}")
            break

if __name__ == '__main__':
    print('============== Road to Debt Free ================')
    balance = int(input('Remaining Debt: (eg. 10400)\n'))
    annualInterestRate = float(input('Annual Interest Rate: (eg. 0.02)\n'))
    months = int(input('Intended Months for Repayment: (eg. 14)\n'))
    Fix_credit_payment(balance, annualInterestRate, months)
