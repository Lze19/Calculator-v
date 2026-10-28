
#CLI CAlCULATOR

a, b = map(int, input("Input 2 Number:").split())
print("List of math operation taht you can use:")
print("Addition(+), Subtraction(-), Multiplication(x or *), Division(: or /), Exponent(^)")
operation = input("Input Operation:")

def calculation(first_number, scnd_number):
    if operation == "+":
        