
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


def output(calculation_result):
    if isinstance(calculation_result, float):
        return f"{calculation_result:.2f}"
    else:
        return (calculation_result)

result = calculation(a, b, op)
print(f"({a}){op}({b}) = {output(result)}")


while isinstance(result, float):  # lanjut hanya kalau hasil masih angka
    loops = input("Add New Operation? (y/n):")
    if loops != "y":
        break
    else:   
        c = float(input("Input Number:"))
        new_op = input("Input Operation:")
        new_result = calculation(result, c, new_op)
        print(output(new_result))
        result = new_result

