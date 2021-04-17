def get_calc(l):
    """
    Создать строку равную всем элементам введенной строки с четными
    индексами. (считая, что индексация начинается с 0, поэтому символы
    выводятся начиная с первого, индексы 0,2,4,6….).
    """
    new_string = ''
    for i in l:
        if l.find(i) % 2 == 0:
            new_string = new_string + i

    return new_string

l = input("Enter string:")

print(get_calc(l))