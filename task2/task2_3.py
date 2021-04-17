def get_calc(l):
    """
    Создать строку равную первым пяти символам введенной строки
    """
    output = l[0:5]
    return output

l = input("Enter string:")

print(get_calc(l))