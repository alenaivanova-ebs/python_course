# 5. На все товары, где есть буква "r", нужно сделать скидку в 20%.
# А если их 2, то 25,5%, и сумму округлить до 2 символов после запятой.
# Рассчитать и вывести на экран стоимость каждого отдельного продукта.
products = {'fruit': ('Apple', 'Pear', 'Banana', 12),
            'vegetables': ('Tomato', 'Onion', 17, 'Cabbage'),
            'berries': ('Blueberry', 'Cranberry', 8, 'Cherry'),
            'finished': ('Carrot', 'Watermelon')}
def find_occurrences(s, ch):
    list_with_indexes =  [i for i, letter in enumerate(s) if letter == ch]
    return len(list_with_indexes)

products_with_price = {}
for item in products:
    if item != 'finished':
        for value in products.get(item):
            if type(value) is not str:
                price = value
        for value in products.get(item):
            if type(value) is str:
                products_with_price[value] = price

products_with_occur = {}
for item in products_with_price:
    products_with_occur[item] = find_occurrences(item, 'r')

print(products_with_price)
for item in products_with_price:
    if products_with_occur.get(item) == 1:
        products_with_price[item] = round(products_with_price.get(item) * 0.8, 2)
    elif products_with_occur.get(item) >= 2:
        products_with_price[item] = round(products_with_price.get(item) * 0.745, 2)
print(products_with_price)
