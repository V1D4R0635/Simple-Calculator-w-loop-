while True:
    x = float(input("First number: "))
    y = float(input("Second number: "))

    Choice_Operator = input("Enter an Operator: ")

    if Choice_Operator == '+':
        Sum = x + y 
        print(f"The Sum of {x} and {y} is: {Sum}")

    elif Choice_Operator == '-':
        Dif = x - y
        print(f"The Difference of {x} and {y} is: {Dif}")
    
    elif Choice_Operator == '*':
        Prod = x * y
        print(f"The Product of {x} and {y} is: {Prod}")

    elif Choice_Operator == '/':
        if y != 0:
            Quo = x / y
            print(f"The Quotient of {x} and {y} is: {Quo}")
        else:
            print("Invalid Option")

    else:
        print("Invalid Choice")

    Continue = input("Do you want to do another calculation y/n? ")

    if Continue != 'y':
        break
