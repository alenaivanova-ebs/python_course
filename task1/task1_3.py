def get_calc(l):
    """
    Дана длина ребра куба.
    Найти объем куба и площадь его боковой поверхности.
    """
    s = l**2
    v = l**3
    output = f"S is {s}. V is {v}"
    return output

l = float(input("Enter l:"))

print(get_calc(l))