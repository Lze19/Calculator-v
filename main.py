
#CLI CAlCULATOR

#=====================Funtions=============================
def input_two_number():
    while True:
        try:
            first, second = map(float, input("Input 2 Number: ").split())
            return first, second
        except ValueError:
            print("Enter exactly two numbers separated by a space, for example: 5 3")

def input_new_number(new_number):
    while True:
        try:
            return float(input(new_number))
        except ValueError:
            print("That is not a number. Try again.")

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
        elif first_number < 0 and scnd_number % 1 != 0:
            return "Undefined"
        else:
            try:
                return first_number**scnd_number
            except OverflowError:
                return "Number Too Large"
    else:
        return "Error"


def output(calculation_result):
    if isinstance(calculation_result, float):
        return f"{calculation_result:.2f}"
    else:
        return (calculation_result)


#=============================MAIN==============================================
a, b = input_two_number()
print("List of math operation that you can use:")
print("Addition(+), Subtraction(-), Multiplication(x or *), Division(: or /), Exponent(^)")
op = input("Input Operation:")


result = calculation(a, b, op)
if isinstance(result, float):
    print(f"({a}){op}({b}) = {output(result)}")
else:
    print(result)


while isinstance(result, float):
    loops = input("Add New Operation? (y/n):")
    if loops != "y":
        print()
        break
    else:   
        c = input_new_number("Input Number:")
        new_op = input("Input Operation:")
        new_result = calculation(result, c, new_op)
        if isinstance(new_result, float):
            print(f"({result}){new_op}({c}) = {output(new_result)}")
        else:
            print(new_result)
        result = new_result