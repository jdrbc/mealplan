from PIL import Image
import pytesseract
import argparse
import click
import re
import os.path

def write_recipe(recipe, title):
    filename = title.replace(' ', '_').lower() + '.md'
    filepath = f'recipes/{filename}'
    if os.path.isfile(filepath) and not click.confirm(f'overwrite {filepath}'):
        i = 1
        while os.path.isfile(filepath):
            filename = f'{title}_{i}.md'
            filepath = f'recipes/{filename}'
    f = open(filepath, 'w')
    f.write(recipe)
    return filepath

def format_recipe(recipe, image_filename, title):
    """Add title, image, and sub headings"""
    # relative to the recipes folder
    image_path = image_filename.replace('recipes', '.')
    header = f'# {title}\n[source]({image_path})\n'
    recipe = re.sub(r'^\s*ingredients\s*$', '## Ingredients', recipe, count=1, flags=re.IGNORECASE|re.MULTILINE)
    recipe = re.sub(r'^\s*((instructions)|(directions))\s*$', '## Directions',
                    recipe, count=1, flags=re.IGNORECASE | re.MULTILINE)
    return header + recipe

def read_title(recipe):
    for line in recipe.splitlines():
        if line.isspace():
            continue
        else:
            return click.prompt('enter title: ', default=line)

@click.command()
@click.argument('image_filename', type=click.Path(exists=True))
def import_recipe(image_filename):
    recipe = pytesseract.image_to_string(Image.open(image_filename))
    title = read_title(recipe)
    recipe = format_recipe(recipe, image_filename, title)
    filename = write_recipe(recipe, title)
    click.edit(filename=filename)

if __name__ == '__main__':
    import_recipe()


