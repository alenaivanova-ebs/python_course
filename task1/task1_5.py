def get_calc(a, b):
    """
    Даны катеты прямоугольного треугольника.
    Найти его гипотенузу и площадь.
    """
    c = (a**2 + b**2)**(1/2)
    s = a*b/2

    output = f"Gipotenuza = {c}. S = {s}. "
    return output

a = float(input("Enter a:"))
b = float(input("Enter b:"))

print(get_calc(a, b))

