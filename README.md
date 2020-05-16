# mealplan
CLI Markdown Meal Planner

## Description

A command line interface meal planner. 

The meal planner allows the user to create a meal plan from recipes stored in the recipe folder.

It then creates a markdown file of the meal plan & a shopping list for the chosen meals.

The `import.py` script will either import from a URL or prompt you for information about the meal & generate a recipe in the format that the meal planner script expects.

## Installation

Install pipenv

`pip install pipenv`

Install dependencies

`pipenv install`

Activate pipenv shell

`pipenv shell`

Create a mealplan!

`python mealplan.py`

## Sample usage

See [sample meal plan](./sample_meal_plan.md) & [sample shopping list](./sample_shopping_list.md).

    (.venv) jdr@LAPTOP-HDNJVE5H:/mnt/c/Users/jroge/projects/meal-plan$ python mealplan.py 
    number of meals [3]: 6

    ====== MEAL PLAN =======

    1. Panfriend Falafel Bowl
    2. Vietnamese Vermicelli Bun Bowl
    3. Bulgar Wheat Tacos
    4. Smokies
    5. Minestrone
    6. Panfriend Falafel Bowl

    ========================

    [r] => regenerate
    [Number] => replace meal
    [Enter] => happy with plan
    : 3


    Options to replace Bulgar Wheat Tacos:
    1. Smokies
    2. Tomato Soup
    3. Chunky Potato Soup
    4. Crunchy Vietnamese Chicken & Rice Salad
    5. Margarita Pizza
    --------------
    [Number] => choose meal
    [Enter] => regenerate / search
    : 5


    ====== MEAL PLAN =======

    1. Panfriend Falafel Bowl
    2. Vietnamese Vermicelli Bun Bowl
    3. Margarita Pizza
    4. Smokies
    5. Minestrone
    6. Panfriend Falafel Bowl

    ========================

    [r] => regenerate
    [Number] => replace meal
    [Enter] => happy with plan
    : 5


    Options to replace Minestrone:
    1. Fish Stew
    2. Panfriend Falafel Bowl
    3. Minestrone
    4. Crunchy Vietnamese Chicken & Rice Salad
    5. Crispy Fish Taco Bowls
    --------------
    [Number] => choose meal
    [Enter] => regenerate / search
    : bu


    Options containing 'bu' to replace Minestrone:
    1. Bulgar Wheat Tacos
    2. Chicken Burrito Bowls
    3. Vietnamese Vermicelli Bun Bowl
    --------------
    [Number] => choose meal
    [Enter] => regenerate / search
    : 1


    ====== MEAL PLAN =======

    1. Panfriend Falafel Bowl
    2. Vietnamese Vermicelli Bun Bowl
    3. Margarita Pizza
    4. Smokies
    5. Bulgar Wheat Tacos
    6. Panfriend Falafel Bowl

    ========================

    [r] => regenerate
    [Number] => replace meal
    [Enter] => happy with plan
    : 6


    Options to replace Panfriend Falafel Bowl:
    1. Vietnamese Vermicelli Bun Bowl
    2. Bulgar Wheat Tacos
    3. Moosewood_Chili
    4. Minestrone
    5. Crispy Fish Taco Bowls
    --------------
    [Number] => choose meal
    [Enter] => regenerate / search
    : sp


    Options containing 'sp' to replace Panfriend Falafel Bowl:
    1. Crispy Fish Taco Bowls
    2. Spaghetti And Meatballs
    --------------
    [Number] => choose meal
    [Enter] => regenerate / search
    : 2


    ====== MEAL PLAN =======

    1. Panfriend Falafel Bowl
    2. Vietnamese Vermicelli Bun Bowl
    3. Margarita Pizza
    4. Smokies
    5. Bulgar Wheat Tacos
    6. Spaghetti And Meatballs

    ========================

    [r] => regenerate
    [Number] => replace meal
    [Enter] => happy with plan
    : 
    printing shopping list for 6 meals
