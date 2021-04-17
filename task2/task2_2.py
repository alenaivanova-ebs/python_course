def get_calc(l):
    """
    Создать строку равную предпоследнему символу введенной строки.
    """
    output = l[-2]
    return output

l = input("Enter string:")

print(get_calc(l))