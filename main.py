#Operator between Number 1 and Number 2
operator = ""

running = True
while running:
    print("To use the calculator choose the operator you want:\n + for addition \n - for Substraction \n *  for multiplication \n /  for division \n")
    operator = input("Enter your operator: ")

    # funtion for substraction
    def substract(n1, n2):
        print(n1 - n2)

    # funtion for addition
    def add(n1, n2):
        print(n1 + n2)

    # funtion for multiplication
    def multiply(n1, n2):
        print(n1 * n2)

    # funtion for division
    def divide(n1, n2):
        print(n1 / n2)


    #Number 1 
    num1 = int(input("Enter your num1: "))

    #Number 2 
    num2 = int(input("Enter your num2: "))

    #logic
    if operator == "-":
        #try typing 10 in num1
        if num1 == 10:
            print(98)
        else:
            substract(num1, num2)
    elif operator == "+":
        add(num1, num2)
    elif operator == "*":
        multiply(num1, num2)
    elif operator == "/":
        divide(num1, num2)
    else:
        print("error: pls type only the charecter that are listed")

    ask = input("Do you want to use again: (y/n)")
    if ask != "y":
        running = False
