#Final Exam

#Name : Mykhailo Hnylytskyi T00257938

#First year Group X

login = input("Please enter yor login ID: ") # Ask user to enter the login and reads it
total = 0           #Total price
expensive = 0       #Price of the most expensive product
number = 0          #Number of the product
less40 = 0          #Number of product cost less than €40
more100 = 0         #Number of product cost more than €100
first = login[0]    #First character of the login
last = login[5]     #Last character of the login
expensivename = "0" #Name of the most expensive product
enter = "0"         #Name of the product entered

if len(login)==6 and first.isalpha() and last.lower()=="x": #Checks login to be suitable according to rules
    print("*"*10,"Valid input...proceeding..", "*"*10)
    while enter != "":                                      #The loop starts if the login is valid
        enter = input("Enter the product name: ")           #Reads first product's name
        if enter != "":
            number += 1     #Adds 1 to product number so than the numeration is controlled
            price = float(input("Enter the price of the product: "))
            total = total + price   #Adds all the prices together
            if price < 40:      
                less40 += 1     #If the price less than €40, it adds 1 to number of products with price less than €40
            if price > 100:
                more100 += 1    #If the price more than €100, it adds 1 to number of products with price more than €100
            if number == 1 or price > expencive:
                expensive = price #The first number is the greatest, so the most expensive thing will be 1st product or product with price more than 1st product
                expensicename = enter #Changes the name of the most expensive product
        else:
            break
    if number == 0:
        print("No products entered!") #If there are no products, it outputs a message
    else:
        over100=more100 / number * 100 #Formula to find percentage of products with price more than €100
        average = total / number #Formula to find the average cost
        print("*"*25,"Your relsults","*"*25)
        print("Total number of product: ", str(number)) #Outputs the number of products
        print("Total cost is %.2f" %(total)) #Outputs the total price
        print("\n\n","*"*10,"Average cost per product: %.2f" %(average)) #Outputs the average price
        print("%.0f" %(less40), " products cost less than €40: ") #Outputs the number of products with price less than €40
        print("%.2f" %(over100), " % of the products cost more than €100!") #Outputs the percentage of products with price more than €100
        print("\nMost expensive product is: ", expensivename, "(Cost: %.2f", expensive, ")") #Outputs the name and the price of the most expensive product
else:
    print("Ivalid login: Lenght is", str(len(login)), ", First character is ", first, ", Last character is ", last) #Outputs the message with information about the login ID, if user enters the wrong one
if number != 0 and len(login)==6 and first.isalpha() and last.lower()=="x":
    print("*"*10, 3*"Ho!", "*"*20)  #Changes the output according to user's decision
else:
    print("*"*10, 3*"Ho!", "*"*10, "Program Exiting")
