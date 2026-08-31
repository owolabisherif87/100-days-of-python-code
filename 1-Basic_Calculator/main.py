print("========= Basic Calculator =========")

operators = ["+", "-", "/", "*"]

print(f"This calculator can perform {", ".join(operators)} operations.")
print("Enter an expression e.g 2 + 2, (2 + 2) / 2 and press enter.\nEnter 'Exit' to close the calculator.\n")

while True:
    expr = input("")

    if expr.lower() == "exit":
        break

    try:
        print(eval(expr, globals={"__builtins__": None}))
    except SyntaxError as err:
        print("Enter a valid expression.")
    except TypeError as error:
        print("Expression Not Allowed.")
