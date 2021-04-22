fruit = ('apple', 'pear', 'cherry', 'banana', 12)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)

# 1. На склад поступил новый товар. Надо пересмотреть склад и исправить ошибки, сделать первую букву заглавной.
# Так же сделать все типы товаров должны быть неизменяемыми, чтобы кто-то случайно не перепутал их снова.
# В овощи забыли добавить капусту. (Цифра в категории - это цена товара этого типа.)
def convert_to_camelcase(lt):
    new = []
    for item in lt:
        if type(item) is str:
            new.append(item.title())
        else:
            new.append(item)
    lt = tuple(new)
    return lt

fruit = list(fruit)
berries = list(berries)

fruit.remove('cherry')
berries.append('cherry')
berries.remove('watermelon')
fruit.append('watermelon')
vegetables.append('cabbage')

print(convert_to_camelcase(fruit))
print(convert_to_camelcase(vegetables))
print(convert_to_camelcase(berries))

# 2. Для удобства хранения, нужно объединить все товары в один объект, при этом сохранить структуру типов.
products = {}
products['fruit'] = convert_to_camelcase(fruit)
products['vegetables'] = convert_to_camelcase(vegetables)
products['berries'] = convert_to_camelcase(berries)
products['finished'] = []
print(products)

# 3. На складе закончились морковка и арбузы. Надо перенести их в категорию "finished".
def add_elements_to_finished(str):
    for item in products:
        for value in products.get(item):
            if value == str:
                tpl = products.get(item)
                lst = list(tpl)
                lst.remove(value)
                products[item] = tuple(lst)
                tpl_unfinished = products['finished']
                lst_unfinished = list(tpl_unfinished)
                lst_unfinished.append(value)
                products['finished'] = tuple(lst_unfinished)

add_elements_to_finished('Carrot')
add_elements_to_finished('Watermelon')
print(products)

# 4. Если название продукта длиннее 6 символов, нужно отображать только первые 6.
def cut_till_6_symboles(lt):
    new = []
    for item in lt:
        if type(item) is str:
            new.append(item[0:6])
        else:
            new.append(item)
    lt = tuple(new)
    return lt

for item in products:
    print(item + ":")
    print(cut_till_6_symboles(products.get(item)))

