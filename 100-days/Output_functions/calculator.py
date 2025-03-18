operations_symbols = ['+','-','/','*']

def operation_options():
    for symbol in operations_symbols:
        print(symbol)

def validate_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please provide a valid number")


def validate_operation_selection(prompt):
    
    while True:
        operation = input(prompt)
        if operation in operations_symbols:
            return operation
        print("Invalid option")


def operate(n1,n2, operator):
    match operator:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "/":
            return n1 / n2 if n2 != 0 else "Error division by zero"
        case "*":
            return n1 * n2
        
last_value = 0

new_calculation = True



while True:

    if new_calculation:
        n1 = validate_float("First number: ")
    else:
        n1 = last_value

    operation_options()
    operator = validate_operation_selection("Select an operation option: ")
    n2 = validate_float("Second number: ")

    result= operate(n1,n2,operator)
    
    if isinstance(result, str):  # Error case
        print(result)
    else:
        last_value = result
        print(f"Result: {last_value}")

    if input("Do you want to exit calculator[yes/no]") == 'yes':
        print("Thanks for using our calculator!")
        break

    new_calculation = input("Would you like to operate using the last value [yes/no]" ) == "no"

 
        

        






