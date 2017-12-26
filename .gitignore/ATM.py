'''
Erika Fortune
Purpose: to access a customers bank account
'''
total=100
while(True):
    username=input("Enter your username:")
    while(username!= "efortune"):
        username=input("Enter your username:")
    password=input("Enter your password:")
    while(password!= "orange21"):
        password=input("Enter your password:")
    print()
    print("1.withdrawal")
    print("2.deposit")
    print("3.balance checks")
    print("4.logout")
    action=input("Choose what you would like to do:")
    while(action!="logout"):
        if(action=="withdrawal"):
            amount=int(input("How much would you like to withdrawal?"))
            if(amount>0 and amount<total):
                total=total-(amount)
                num1="your account balance: $"
                print(num1+str(total))
                action=input("Choose what you would like to do next:")
            else:
                print("you cannot withdrawal that much money")
        if (action=="deposit"):
            amount=int(input("How much would you like to deposit?"))
            if(amount>0 and amount<total):
                total=total+(int(amount))
                num1="your account balance: $"
                print(num1+str(total))
                print()
                print("1.withdrawal")
                print("2.deposit")
                print("3.balance checks")
                print("4.logout")
                action=input("Choose what you would like to do next:")
            else:
                print("you cannot deposit that much money")   
        if(action=="balance checks"):
            num1="your account balance: $"
            print(num1+str(total))
            action=input("Choose what you would like to do next:")

    
