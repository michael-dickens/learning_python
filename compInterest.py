# Compound interest calculator, assumes only an annual interest compounding

def SWR(balance, swr): #Takes the CI balance and turns it into yearly and monthly incomes based on safe withdrawal rates
    safeAnnualIncome = balance * swr
    safeMonthlyIncome = safeAnnualIncome / 12 #convert to monthly income
    print('With a safe withdrawal rate of: ' + str(swr*100) + '% your yearly gross income will be about: ' + str(round(safeAnnualIncome, 2))
    + ' with a monthly gross income of: ' + str(round(safeMonthlyIncome, 2)))

while True:
    try:
        p = int(input("What is your current principal: ")) #Current principal 
        r = float(input("What is your interest rate in percent (typically 6-8): ")) / 100 #gets interest rate as decimal percent
        t = int(input('How many years invested: ')) 
        a = int(input('What are your yearly additions: '))
        addAtEnd = ''

        while True:
            try:
                addAtEnd = input('Are you making the addtion at the end of the year? Type y or n: ')
                addAtEnd = addAtEnd.lower()
                if addAtEnd == 'y' or addAtEnd == 'n':
                    break
            except ValueError:
                print('Error: invalid inputs')   
        break

    except ValueError:
        print('Error: invalid inputs')

if addAtEnd == 'n':
    balance = p*((1+r)**t) + a*(((1+r) ** (t+1) - (1+r))/r) #compunding interest formula w/ yearly additions
    balance = round(balance, 2) #rounds down to dollars and cents
else:
    balance = p*((1+r)**t) + a*((((1+r) ** t) - 1)/r) # adding money at the end of the year takes a year off of compounding
    balance = round(balance, 2) #rounds down to dollars and cents

print('Your balance at the end of ' + str(t) + ' years is: ' +  str(balance))
SWR(balance, .04)
SWR(balance, .03)



