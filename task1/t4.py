def get_calc(a, b):
    """
    Даны два действительных числа. Найти среднее арифметическое и
   среднее геометрическое этих чисел
    """
    avg = (a + b)/2
    geometric_mean = (a*b)**(1/2)

    output = f"Average is {avg}. Geometric mean is {geometric_mean}. "
    return output


a = float(input("Enter a:"))
b = float(input("Enter b:"))


print(get_calc(a, b))
