from datetime import datetime as dt
from random import randrange


database = {'0030692791':[376800,'Tijani','Airbender'],
            '0030692790':[678900,'David','Davidpass'],
            '0030692789':[5428690,'Rowland','Rowsmary'],
            '0030692788':[4910000.87,'Courage','Puissance']
            }
dicKeys = database.keys()
dicValues = database.values()

def intake():

    while True:
        regQuest = input('Please Enter your account Number :\n')
        userPassword = input('Please Enter your secret password :\n')
        if (regQuest in dicKeys):
            if (userPassword==database[regQuest][2]):
                WelcomeMessage = 'Welcome back '+ database[regQuest][1]
                break
            else:
                print('Invalid Password, Please try again')
        else:
            print('This user does not exist')

    return regQuest,WelcomeMessage

def login():
    print('''\nDo you have an account?, If Yes, press 1, If No press 2''')
    promt = int(input('Select Option:\n'))
    if promt ==1:
        p = intake()
        print(p[1])
        x=str(dt.now())
        print('You Logged in to your account at: {}'.format(x.split('.')[0]))
        print('''\nWhat Operation do you want to perform \n\t
    Press 1 for cash withdrawal\n\t
    Press 2 for  deposit\n\t
    Press 3 to contact Customer Support Center\n\t
    Press 4 to Logout of your account.''')

        Option_Chosen = int(input("Enter You Preferred Option : \n"))

        if Option_Chosen == 1:
            cashWithdrawal()

        elif Option_Chosen == 2:

            cashDeposit()

        elif Option_Chosen == 3:
            customerSupport()

        elif Option_Chosen == 4:
            logout()
        
        else:
            print('Invalid Input, Please try again.')
            login()

    elif promt == 2:
        print('Will you like to register?')
        userOption = int(input('If yes press 1, if No press 2 to exist\n'))
        if userOption ==1:
            register()
        elif userOption ==2:
            print('Thank you for your interest...')
            exit()
        else:
            exit()
    else:
        pass
    
    #return regQuest


def register():
    print('Welcome to the registration room')
    firstName = input('Enter your first name:\n').capitalize()
    lasttName = input('Enter your last name:\n').capitalize()
    email = input('Enter your email address:\n')
    password = input('Enter your first password:\n')
    openingBalance = float(input('Enter your Opening Balance:\n'))
    gender = input('What is your gender:\n').strip().title()
    fullName = firstName.strip() +' '+lasttName.strip()
    acc = accGeneration()
    if acc not in dicKeys:
        database.update({acc:[openingBalance, fullName, password]})
    else:
        print('input exist')

    if gender == 'Male':
        accMessage = 'Dear Mr. '+fullName+' your account number is ' + acc
    elif gender == 'Female':
        accMessage = 'Dear Mrs./Ms. '+fullName+' your account number is ' + acc
    else:
        accMessage = 'Dear '+fullName+' your account number is ' + acc
    print(accMessage)


def logout():
    goodbyeMessage = 'Thank you for banking with us '
    print(goodbyeMessage)

def cashDeposit(): 
    amtDeposit =  int(input("Enter Amount to deposit :\n"))
    print("Your Current Balance is {}".format(amtDeposit))

def cashWithdrawal():
    amtToWithdraw =  int(input("Enter Amount to deposit :\n"))
    print("Your Current Balance is {}".format(amtToWithdraw))

def customerSupport():

    print('''To speak with our customer service :\n\t
    Choose 1 to be transferred to a customer service agent\n
    Choose 2 to sent a mail compalaint\n''')
    custServOption = int(input('Enter your preferred option\n'))
    if custServOption == 1:
        print('Please wait while we transfer your call to our customer service agent...')
    elif custServOption == 2:
        email = input('Please Enter your e-mail address: \n')
        print('You will receive an email in ',email)
    else:
        print('You have entered the wrong option')

def accGeneration():
    accNumber = randrange(1000000000,9999999999)
    return str(accNumber)

#cashDeposit()
login()
#print(cashWithdrawal())
#register()
#print(database)