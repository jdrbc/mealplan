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
from shoppinglist import print_shopping_list

@dataclass
class Meal:
    name: str = 'unknown'
    url: str = 'unknown'
    ingredients: List[str] = field(default_factory=list)

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@lru_cache(maxsize=None)
def get_dir_files(dir):
    return [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]

def read_meal(file_name):
    logger.debug(f'reading meal {file_name}')
    url = f'./recipes/{file_name}'
    recipe = open(url, 'r')

    mode = 'read_title'
    title = 'unknown'
    ingredients = []
    for num, line in enumerate(recipe, 1):
        if line.isspace():
            continue
        elif mode == 'read_title':
            match = re.search('# (.*)', line)
            if match is not None:
                title = match.group(1)
                mode = 'find_ingredient_section'
                logger.debug(f'found title at line {num}')
        elif mode == 'find_ingredient_section':
            match = re.search('# ingredients', line, re.IGNORECASE)
            if match is not None:
                mode = 'read_ingredient'
                logger.debug(f'found ingredients section at line {num}')
        elif mode == 'read_ingredient':
            # figure out if done
            match = re.search('##\s*(Directions|Instructions)', line, re.IGNORECASE)
            if match is not None:
                mode = 'done'
            else:
                match = re.search('^\s*-\s*(.*)', line)
                if match is not None:
                    ingredients.append(match.group(1))
        else:
            break
    logger.debug(f'meal read complete. found {len(ingredients)} ingredients.')
    logger.debug(f'finished parsing at line {num} in mode {mode}')
    return Meal(title.title(), url, ingredients)

def print_meals(meals):
    if not meals:
        click.echo('no meals!')
    else:
        i = 1
        for meal in meals:
            click.echo(f'{i}. {meal.name}')
            i += 1
            
def print_meal_plan(meals):
    click.echo('\n\n====== MEAL PLAN =======\n')
    print_meals(meals)
    click.echo('\n========================\n')

def replace_meal(meals, meal_num, search=None):
    if search is None:
        click.echo(f'\n\nOptions to replace {meals[meal_num-1].name}:')
    else:
        click.echo(f'\n\nOptions containing \'{search}\' to replace {meals[meal_num-1].name}:')

    meal_options = get_meals(5) if search is None else get_meals(num=None, search=search)
    print_meals(meal_options)
    click.echo('--------------')
    click.echo('[Number] => choose meal')
    click.echo('[Enter] => regenerate / search')
    resp = click.prompt('', default='regenerate', show_default=False)
    if (is_int(resp)):
        resp = int(resp)
        if resp in range(1, len(meal_options) + 1):
            replacment = meal_options[resp-1]
            meals[meal_num - 1] = replacment
            return meals
        else:
            click.echo('sorry, invalid selection')
            return replace_meal(meals, meal_num)
    elif resp == 'regenerate':
        return replace_meal(meals, meal_num)
    else:
        return replace_meal(meals, meal_num, resp)


def confirm_meals(meals):
    print_meal_plan(meals)
    click.echo('[r] => regenerate')
    click.echo('[Number] => replace meal')
    click.echo('[Enter] => happy with plan')
    resp = click.prompt('', default='y', show_default=False)
    if resp == 'r':
        return confirm_meals(get_meals(len(meals)))
    elif resp == 'y':
        return meals
    
    if is_int(resp):
        resp = int(resp)
        if resp in range(1, len(meals) + 1):
            return confirm_meals(replace_meal(meals, resp))
    click.echo('sorry, invalid selection')
    return confirm_meals(meals)
        

def get_meals(num=None, search=None):
    recipe_file_names = get_dir_files('recipes')

    if search is not None:
        terms = search.split(' ')
        recipe_file_names = filter(lambda file_name: any(term in name_part for term in terms for name_part in file_name.split('_')), recipe_file_names)

    if num is not None:
        recipe_file_names = random.sample(recipe_file_names, num)

    meals = []
    for name in recipe_file_names:
        meals.append(read_meal(name))
    return meals

def print_plan(meals):
    env = Environment(
        loader=PackageLoader('mealplan', 'templates')
    )
    template = env.get_template('meal_plan_template.md')
    f = open('./#meal_plan.md', 'w')
    f.write(template.render(meals=meals))

@click.command()
def build_plan():
    nummeals = int(click.prompt('number of meals', default='3', show_default=True))

    # get some meals
    meals = get_meals(nummeals)
    meals = confirm_meals(meals)

    # print suggested plan
    print_plan(meals)

    # print shopping list
    print_shopping_list(meals)

if __name__ == '__main__':
    logger.disable(__name__)
    build_plan()
