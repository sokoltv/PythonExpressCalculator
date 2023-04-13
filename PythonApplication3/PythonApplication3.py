while True:
    expres = input("Enter an expression: \n")
    try:
        result = eval(expres)
        print("The result is:\n", result)
        
    except:
        print("Invalid expression. Please try again.")
