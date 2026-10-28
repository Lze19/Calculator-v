
#CLI CAlCULATOR

a, b = map(float, input("Input 2 Number:").split())
print("List of math operation that you can use:")
print("Addition(+), Subtraction(-), Multiplication(x or *), Division(: or /), Exponent(^)")
c = input("Input Operation:")

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

print(f"{a}{c}{b} = {calculation(a, b, c):.2f}")