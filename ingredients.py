DAIRY = 'dairy'
MEAT = 'meat'
SPICES = 'spices'
SAUCES = 'sauces and condiments'
BREAD = 'bread and bakery'
BAKING = 'baking'
VEGGIES = 'veggies'
CANNED = 'canned'
GRAINS = 'grains'
MISC = 'misc'
PASTA = 'pasta'
FRUIT = 'fruit'

CATEGORY_TO_LONG_INGREDIENTS = {
    SPICES: [
        'garlic powder',
        'chili powder',
        'bay leaves',
        'bay leaf'
    ],
    SAUCES: [
        'peanut butter'
    ],
    BAKING: [
        'lemon juice'
    ],
    VEGGIES: [
        'green bean',
        'bok choy',
        'bell pepper',
        'fresh basil'
    ],
    CANNED: [
        'coconut milk'
    ],
    GRAINS: [
        'bulgar wheat'
    ],
    MISC: [
        'chili sauce'
    ]
}

CATEGORY_TO_INGREDIENTS = {
    DAIRY: [
        'milk',
        'egg',
        'cheese',
        'butter',
        'cream',
        'yogurt',
        'feta'
    ],
    MEAT: [
        'beef',
        'chicken',
        'pork',
        'cod',
        'fish',
        'salmon',
        'sausage',
        'meat'
    ],
    SPICES: [
        'salt',
        'pepper',
        'powder',
        'oregano',
        'thyme',
        'cumin',
        'seasoning',
        'basil',
        'cinnamon',
        'turmeric',
        'ground'
    ],
    GRAINS: [
        'rice',
        'grain',
        'quinoa',
        'bulgur'
    ],
    BREAD: [
        'buns',
        'bread',
        'sandwich',
        'wrap'
    ],
    BAKING: [
        'flour',
        'sugar',
        'honey',
        'yeast'
    ],
    SAUCES: [
        'mustard',
        'ketchup',
        'relish',
        'salsa',
        'mayo',
        'tahini'
    ],
    PASTA: [
        'pasta',
        'spaghetti'
    ],
    CANNED: [
        'bean'
        'can',
        'chickpeas'
    ],
    FRUIT: [
        'lime',
        'lemon',
        'apples',
        'avocado',
        'avo',
    ],
    VEGGIES: [
        'chiles',
        'shallot'
        'peas',
        'parsley',
        'scallion',
        'spinach'
        'lettuce',
        'corn',
        'jalapeno',
        'celery',
        'carrot',
        'potato',
        'squash',
        'zucchini',
        'onion',
        'scallions',
        'cucumber',
        'garlic',
        'ginger',
        'radishes',
        'cabbage',
        'cilantro',
        'mint',
        'lemon',
        'tomato'
    ]
}

def flip_dict(key_to_list):
    ret = {}
    for key in key_to_list.keys():
        values = key_to_list[key]
        for value in values:
            ret[value] = key
    return ret

INGREDIENT_TO_CATEGORY = flip_dict(CATEGORY_TO_INGREDIENTS)
LONG_INGREDIENT_TO_CATEGORY = flip_dict(CATEGORY_TO_LONG_INGREDIENTS)