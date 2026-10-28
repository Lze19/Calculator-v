
#CLI CAlCULATOR

a, b = map(int, input("Input 2 Number:").split())
print("List of math operation that you can use:")
print("Addition(+), Subtraction(-), Multiplication(x or *), Division(: or /), Exponent(^)")
operation = input("Input Operation:")

def calculation(first_number, scnd_number):
    if operation == "+":
        return first_number + scnd_number
    elif operation == "-":
        return first_number - scnd_number
    elif operation == "x" or operation == "*":
        return first_number*scnd_number
    elif operation == ":" or operation == "/":
        return first_number/scnd_number
    elif operation == "^":
        return first_number**scnd_number
    else:
        return "Error"

print(f"{a}{operation}{b} = {calculation(a, b)}")