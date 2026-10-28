
#CLI CAlCULATOR

a, b = map(float, input("Input 2 Number:").split())
print("List of math operation that you can use:")
print("Addition(+), Subtraction(-), Multiplication(x or *), Division(: or /), Exponent(^)")
op = input("Input Operation:")

def calculation(first_number, scnd_number,operation):
    if operation == "+":
        return first_number + scnd_number
    elif operation == "-":
        return first_number - scnd_number
    elif operation == "x" or operation == "*":
        return first_number*scnd_number
    elif operation == ":" or operation == "/":
        if scnd_number == 0:
            return "Undefined"
        else:
            return first_number/scnd_number
    elif operation == "^":
        return first_number**scnd_number
    else:
        return "Error"


def validating_ans(result_number):
    if result_number.isnumeric() == True:
        return (f"({a}){op}({b}) = {calculation(a, b, op):.2f}")
    else:
        return result_number

operating = calculation(a,b, op)
print(validating_ans(operating))