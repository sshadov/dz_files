cook_book = dict()
with open("recipies.txt", "r", encoding='utf8') as file:
    for line in file:
        dish_name = line.strip()
        num = int(file.readline().strip())
        for i in range(num):
            cook_book_ingridients = dict()
            ing = file.readline().split("|")
            cook_book_ingridients['ingridient_name'] = ing[0]
            cook_book_ingridients['quantity'] = ing[1]
            cook_book_ingridients['measure'] = ing[2].strip('\n')
            if dish_name in cook_book:
                cook_book[dish_name] += [cook_book_ingridients]
            else:
                cook_book[dish_name] = [cook_book_ingridients]
        next_dish = file.readline().strip()

    print(f'{cook_book}')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = dict()
    a = 0
    b = 0
    for dish in dishes:
        for ingridients in cook_book[dish]:

            if ingridients['ingridient_name'] in shop_list:
                 count_in_shoplist = int(shop_list[ingridients['ingridient_name']]['quantity'])
                 add_count_to_shoplist = int(ingridients['quantity']) * int(person_count) + count_in_shoplist
                 shop_list[ingridients['ingridient_name']]['quantity'] = add_count_to_shoplist
            else:
                shop_list[ingridients['ingridient_name']] = {'measure': ingridients['measure'] , 'quantity': int(ingridients['quantity']) * person_count}
            # shop_list = {[ingridients['ingridient_name']:ingridients['quantity']}
            # print(shop_list)
    return shop_list
    # print(shop_list)
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

