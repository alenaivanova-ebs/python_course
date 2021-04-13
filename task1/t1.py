def get_calc(a, b):
    """
    Даны 2 действительных числа a и b.
    Получить их сумму, разность и произведение
    """
    sum = a + b
    diff = a - b
    multiply = a * b
    output = f"Sum is {sum}. Diff is {diff}. Multiply is {multiply}."
    return output

a = float(input("Enter a:"))
b = float(input("Enter b:"))

print(get_calc(a, b))
