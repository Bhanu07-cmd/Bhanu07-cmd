print("Welcome to the ATM")
restart = 'Y'
chances = 3
balance = 2000.0
while chances >= 0:
    pin = int(input("Please enter your 4 digit password: "))
    if pin == 1234:
        print("You have enterd your pin correctly\n")
        while restart not in ('n', 'NO', 'no', "N"):
            print('Please Press 1 For your balance\n')
            print('Please press 2 To Make a Withdrawl\n')
            print("Please press 3 to Pay\n")
            print("Please press 4 to Return Card\n")
            option = int(input("What would you like to choose ? "))
            if option == 1:
                print("Your Balance is Rs", balance, '\n')
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', "N"):
                    print("Thank You")
                    break
            elif option == 2:
                option = 'y'
                withdrawl = float(input("How Much would like to withdrawl? \nRS10/RS20/RS40/RS60/RS80/RS100 for other enter 1:" ))
                if withdrawl in [10, 20, 30, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print("\nYour bank balance is now Rs ", balance)
                    restart = input("Would like to go back?")
                    print("Thank You")
                    break
                elif withdrawl != [10, 20, 30, 40, 60, 80, 100]:
                    print("Invalid Amount, Please Re-try\n")
                    restart = 'y'
                elif withdrawl ==1:
                    withdrawl = float(input("Please Enter Desired amount:"))
            elif option == 3:
                Pay_in = float(input("How much would like to pay in? "))
                balance = balance + Pay_in
                print("\n Your Balace is now Rs", balance)
                restart = input("Would like to go back?")
                if restart in ('n', 'NO', 'no', "N"):
                    print("Thank You")
                    break
            elif option == 4:
                print("Please wiat whilist your card is Returned.......\n")
                print("Thank you for using our ATM Service")
                break
            else:
                print("Please Enter a correct number. \n")
                restart = 'y'
    elif pin != '1234':
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("\n NO more tries")
            break