
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
        if first_number == 0 and scnd_number < 0:
            return "Undefined"
        else:
            return first_number**scnd_number
    else:
        return "Error"

Result = calculation(a, b, op)
if isinstance(Result, float):
    print(f"({a}){op}({b}) = {Result:.2f}")
else:
    print(Result)