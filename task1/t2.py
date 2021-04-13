def get_calc(x, y):
    """
    Даны действительные числа x и y. Получить (|x| − |y|)/(1+ |xy|)
    """
    result = (abs(x) - abs(y))/(1 + abs(x*y))
    output = f"Result is {result}."
    return output


x = float(input("Enter x:"))
y = float(input("Enter y:"))

print(get_calc(x, y))