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
from ingredients import INGREDIENT_TO_CATEGORY, LONG_INGREDIENT_TO_CATEGORY

IGNORED_INGREDIENTS = ['water']

def print_shopping_list(meals):
    click.echo(f'printing shopping list for {len(meals)} meals')
    
    ingredients = [ingredient for meal in meals for ingredient in meal.ingredients]

    # sort ingredients into categories
    category_to_ingredients = {}
    for ingredient in ingredients:
        cat = find_ingredient_category(ingredient)

        ingredients_in_cat = category_to_ingredients.get(cat, [])
        ingredients_in_cat.append(ingredient)
        category_to_ingredients[cat] = ingredients_in_cat

    env = Environment(
        loader=PackageLoader('mealplan', 'templates')
    )
    template = env.get_template('shopping_list_template.md')

    f = open('./#shopping_list.md', 'w')
    f.write(template.render(categories=category_to_ingredients.keys(), category_to_ingredients=category_to_ingredients))

def find_ingredient_category(ingredient):
    ingredient = ingredient.lower()
    for long_ingredient in LONG_INGREDIENT_TO_CATEGORY.keys():
        if long_ingredient in ingredient:
            return LONG_INGREDIENT_TO_CATEGORY[long_ingredient]

    for word in ingredient.split(' '):
        if word in IGNORED_INGREDIENTS: 
            return None
        if word in INGREDIENT_TO_CATEGORY:
            return INGREDIENT_TO_CATEGORY[word]
    return 'misc'
