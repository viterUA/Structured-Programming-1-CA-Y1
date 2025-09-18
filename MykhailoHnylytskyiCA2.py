#MykhailoHnylytskyi_CA2.py

#Name:Mykhailo Hnylytskyi

#Group X

print("*"*10,"Welcome to the MTU Kerry Banking application","*"*10)

answer = input("Enter your username: ")
password = input("Enter the password: ")

if answer.lower() or password.upper():
    print("Incorrect password - please reset!")
    
if answer.upper() and password.upper():
    print("Please enter an option:\n\n\t\t",
            "1.Reset your password\n\t\t",
            "2.Withdraw money\n\t\t",
            "3. Convert euro to dollars")
    answer2 = input("")
    if answer2 == "1":
        password2 = input("Please enter your new password:\n")
        if password2.isalnum() and password2.lower() and password2.upper():
            print("Password OK - update succeeded!")
        else:
            print("Password change rejected - program will exit")
    if answer2 == "2":
        balance = float(input("Enter your current balance (in euro): "))
        withdraw = float(input("How much do you wish to withdraw?: "))
        print("Withdraw of €", withdraw ,"granted.")
        print("Remaining balance is € ","%.2f" % (balance - withdraw))
    if answer2 == "3":
        euro = float(input("Enter the amount in euro: "))
        print("For €", euro, ",you will receive $","%.2f" %(euro * 1.1))        
        
