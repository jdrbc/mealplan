import sys
from loguru import logger
from jinja2 import Environment, PackageLoader
from dataclasses import dataclass, field
from typing import List
import os
import os.path
import random
import re
import click
from functools import lru_cache
from ingredients import INGREDIENT_TO_CATEGORY, LONG_INGREDIENT_TO_CATEGORY, DAIRY, MEAT, SPICES, SAUCES, BREAD, BAKING, VEGGIES, CANNED, GRAINS, MISC, PASTA, FRUIT

IGNORED_INGREDIENTS = ['water']
PREP_KEYWORDS = [',', 'lightly beaten', 'beaten', 'peeled', 'finely', 'sliced', 'coarsely', 'shredded', 'thinly', 'chopped', 'minced', 'squeezed', 'uncooked', 'cooked', 'diced']
LIST_ORDER = [
    VEGGIES, 
    FRUIT,
    BREAD, 
    MEAT, 
    DAIRY, 
    SPICES, 
    SAUCES, 
    BAKING, 
    CANNED, 
    PASTA, 
    GRAINS, 
    MISC, 
]


def print_shopping_list(meals):
    click.echo(f'printing shopping list for {len(meals)} meals')
    
    ingredients = [ingredient.lower() for meal in meals for ingredient in meal.ingredients]

    ingredients = combine_ingredients(ingredients)

    # sort ingredients into categories
    category_to_ingredients = {}
    for ingredient in ingredients:
        cat = find_ingredient_category(ingredient)
        if cat is not None:
            ingredients_in_cat = category_to_ingredients.get(cat, [])
            ingredients_in_cat.append(ingredient)
            category_to_ingredients[cat] = ingredients_in_cat

    env = Environment(
        loader=PackageLoader('mealplan', 'templates')
    )
    template = env.get_template('shopping_list_template.md')

    f = open('./#shopping_list.md', 'w')
    f.write(template.render(categories=intersection(LIST_ORDER, category_to_ingredients.keys()), category_to_ingredients=category_to_ingredients))

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

# parse out the main ingredient, discard prep info, provide quantity
def combine_ingredients(ingredients):
    main_ingredient_to_quantity = {}
    for raw_ingredient_text in ingredients:
        raw_ingredient_text = remove_prep_keywords(raw_ingredient_text)

        main_ingredient, quantity_text = split_ingredient_and_quantity(raw_ingredient_text)
        if not quantity_text:
            quantity_text = '1'
        quantity_texts = main_ingredient_to_quantity.get(main_ingredient, [])
        quantity_texts.append(quantity_text)
        main_ingredient_to_quantity[main_ingredient] = quantity_texts
    
    # dedupe main ingredients
    all_ingredients = []
    for main_ingredient, quantity in main_ingredient_to_quantity.items():
        if quantity:
            all_ingredients.append(main_ingredient + ' (' + ', '.join(quantity) + ')')
    return all_ingredients

def remove_prep_keywords(raw_ingredient_text):
    # todo remove all?
    for keyword in PREP_KEYWORDS:
        raw_ingredient_text = raw_ingredient_text.replace(keyword, '')
    return raw_ingredient_text

def split_ingredient_and_quantity(raw_ingredient_text):
    'return the keyword, raw ingredient minus keyword (prep, ingredient, quantity)'
    for long_ingredient in LONG_INGREDIENT_TO_CATEGORY.keys():
        if long_ingredient in raw_ingredient_text:
            return (long_ingredient, ' '.join(raw_ingredient_text.replace(long_ingredient, '').split()))

    for word in raw_ingredient_text.split():
        if word in INGREDIENT_TO_CATEGORY:
            return (word, ' '.join(raw_ingredient_text.replace(word, '').split()))
        depluralizedword = depluralize(word)
        if depluralizedword in INGREDIENT_TO_CATEGORY:
            return (depluralizedword, ' '.join(raw_ingredient_text.replace(word, '').split()))
    return raw_ingredient_text, None

def find_ingredient_category(ingredient):
    for long_ingredient in LONG_INGREDIENT_TO_CATEGORY.keys():
        if long_ingredient in ingredient:
            return LONG_INGREDIENT_TO_CATEGORY[long_ingredient]

    for word in ingredient.split(' '):
        if word in IGNORED_INGREDIENTS:
            return None
        if word in INGREDIENT_TO_CATEGORY:
            return INGREDIENT_TO_CATEGORY[word]
        singular_word = depluralize(word) 
        if singular_word in INGREDIENT_TO_CATEGORY:
            return INGREDIENT_TO_CATEGORY[singular_word]
    return 'misc'

def depluralize(word):
    if word.endswith('es'):
        return word.rstrip('es')
    elif word.endswith('s'):
        return word.rstrip('s')
    else:
        return None