import os
import logging



def logger(old_function):

    logging.basicConfig(
    level=logging.INFO, 
    filename = "main1.log", 
    format = "%(asctime)s - %(message)s", 
    datefmt='%H:%M:%S',
    )
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        string_name = old_function.__name__
        info = f'{string_name} {args} {kwargs} {result}'
        logging.info(info)
        return result
        
    return new_function




recipes = []

with open('recipes.txt', 'r', encoding='utf8' ) as rec_fail:
    for text in rec_fail:
        dish_name = text.strip()
        dish = {"name": dish_name, "ingredients": []}
        ingredients_count = rec_fail.readline()
        for ing in range(int(ingredients_count)):
            ingredients = rec_fail.readline()
            name, quantity, measure = ingredients.strip().split(' | ')
            dish ['ingredients'].append({'name': name, 'quantity': quantity, 'measure': measure})
        blank_line = rec_fail.readline()
        recipes.append(dish)

@logger
def get_shop_list_by_dishes(list_dish, people):
    with open('recipes.txt', 'r', encoding='utf8' ) as rec_fail:
        for text in rec_fail:
            dish_name = text.strip()
            dish = {"name": dish_name, "ingredients": []}
            ingredients_count = rec_fail.readline()
            for ing in range(int(ingredients_count)):
                ingredients = rec_fail.readline()
                name, quantity, measure = ingredients.strip().split(' | ')
                dish ['ingredients'].append({'name': name, 'quantity': quantity, 'measure': measure})
            blank_line = rec_fail.readline()
            recipes.append(dish)
    purchases = {}
    for dish in list_dish:
        for dish_book in recipes:
            if dish_book['name'] == dish:
                for ing in dish_book['ingredients']:
                    if ing['name'] not in purchases.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity'])
                        purchases[ing['name']] = {'measure': measure, 'quantity': quantity}
                    
                    elif ing['name'] in purchases.keys():
                        measure = ing['measure']
                        quantity = people * int(ing['quantity']) + int((purchases[ing['name']])['quantity'])
                        purchases[ing['name']] = {'measure': measure, 'quantity': quantity}
    return purchases

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))