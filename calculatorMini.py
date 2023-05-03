# Mini Project in python to build a calculator 
first = input("Enter the first number : ")
second = input("Enter the second number : ") 
operator = input("Enter the operator(+,-,*,/,%) : ")
first = int(first)
second = int(second)
if operator == "+" : 
    print(first+second)
elif operator == "-" : 
    print(first-second)
elif operator == "*" : 
    print(first*second)
elif operator == "/" : 
    print(first/second)
elif operator == "%" : 
    print(first%second)
else : 
    print("Invalid Operation")
