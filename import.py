import click
import re
import os.path
from dataclasses import dataclass
from jinja2 import Environment, PackageLoader


@dataclass
class Recipe:
    title: str = ''
    source: str = ''
    servings: str = ''
    time: str = ''
    ingredients: str = ''
    directions: str = ''

def get_filepath(title):
    filename = title.replace(' ', '_').lower() + '.md'
    filepath = f'recipes/{filename}'
    if os.path.isfile(filepath) and not click.confirm(f'overwrite {filepath}'):
        i = 1
        while os.path.isfile(filepath):
            filename = f'{title}_{i}.md'
            filepath = f'recipes/{filename}'
    return filepath

def build_recipe(recipe):
    env = Environment(
        loader=PackageLoader('mealplan', 'templates')
    )
    template = env.get_template('recipe_template.md')
    return template.render(recipe=recipe)

def import_recipe():
    recipe = Recipe()
    # get name
    recipe.title = click.prompt('Enter name')
    # get source
    recipe.source = click.prompt('Enter source')
    # get prep time
    recipe.time = click.prompt('Enter prep time')
    # get num servings
    recipe.servings = click.prompt('Enter num servings')
    MARKER = '# Enter ingredients above \n'
    recipe.ingredients = click.edit(
        '\n\n' + MARKER).split(MARKER, 1)[0].rstrip('\n')
    # get directions
    MARKER = '# Enter directions above \n'
    recipe.directions = click.edit(
        '\n\n' + MARKER).split(MARKER, 1)[0].rstrip('\n')

    recipetext = build_recipe(recipe)
    filepath = get_filepath(recipe.title)
    open(filepath, 'w').write(recipetext)
    click.edit(filename=filepath)

if __name__ == '__main__':
    import_recipe()
