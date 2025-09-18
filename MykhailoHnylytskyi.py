#MykhailoHnylytskyi.py

#This program pisplays calculation and output the price per ounce for the item
#Note: There are 16 ounces(oz) in a 1 pound(lb)

#Name: Mykhailo Hnylytskyi

#Class: Computuing 1 year Group X

item = input("Enter the item: ")
ounces = float(input("Enter the ounces: "))
total = float(input("Enter the total cost: "))
lb = ounces // 16


print("*"*25, "PRICE PER OUNCE CALCULATOR", "*"*25,
      "\nTotal Ounces\t\tPrice per Ounce", "\n", ounces, "\t\t\t", "    %0.2f"% (total / ounces),
      "\nFor ", lb," lb and", ounces, "ounces of", item, "@ €",total, ", the cost price per ounce is €","%0.2f"% (total / ounces))
print("*"*25, "PRICE PER OUNCE CALCULATOR", "*"*25)
