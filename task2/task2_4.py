def get_calc(l):
    """
    Создать строку равную введенной строку без последних двух символов.
    """
    n = len(l)-2
    output = l[0:n]
    return output

l = input("Enter string:")

print(get_calc(l))