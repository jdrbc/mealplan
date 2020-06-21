DAIRY = 'dairy'
MEAT = 'meat'
SPICES = 'spices'
SAUCES = 'sauces/condiments/oil'
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
        'bay leaf',
        'salt and pepper',
        'black pepper',
        's & p',
    ],
    SAUCES: [
        'peanut butter',
        'fish sauce',
        'olive oil',
    ],
    BAKING: [
        'bread flour',
        'lemon juice',
        'maple syrup',
    ],
    VEGGIES: [
        'green bean',
        'bok choy',
        'bell pepper',
        'fresh basil',
    ],
    CANNED: [
        'coconut milk',
    ],
    GRAINS: [
        'bulgar wheat',
    ],
    MISC: [
        'chili sauce',
        'tortilla chips',
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
        'feta',
        'mozzarella',
    ],
    MEAT: [
        'beef',
        'chicken',
        'pork',
        'cod',
        'fish',
        'salmon',
        'sausage',
        'meat',
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
        'ground',
    ],
    GRAINS: [
        'rice',
        'grain',
        'quinoa',
        'bulgur',
    ],
    BREAD: [
        'bun',
        'bread',
        'sandwich',
        'wrap',
    ],
    BAKING: [
        'flour',
        'sugar',
        'honey',
        'yeast',
    ],
    SAUCES: [
        'mustard',
        'vinaigrette',
        'ketchup',
        'relish',
        'salsa',
        'mayo',
        'tahini',
        'oil',
        'sauce',
    ],
    PASTA: [
        'pasta',
        'spaghetti',
    ],
    CANNED: [
        'bean',
        'can',
        'chickpeas',
    ],
    FRUIT: [
        'lime',
        'lemon',
        'apple',
        'avocado',
        'avo',
    ],
    VEGGIES: [
        'greens',
        'chiles',
        'shallot',
        'peas',
        'parsley',
        'scallion',
        'spinach',
        'lettuce',
        'corn',
        'jalapeno',
        'celery',
        'carrot',
        'potato',
        'squash',
        'zucchini',
        'onion',
        'scallion',
        'cucumber',
        'garlic',
        'ginger',
        'radish',
        'cabbage',
        'cilantro',
        'mint',
        'lemon',
        'tomato',
    ],
    MISC: [
        'almond',
        'peanut',
    ]
}

def flip_dict(key_to_list):
    ret = {}
    for key, items in key_to_list.items():
        for item in items:
            ret[item] = key
    return ret

INGREDIENT_TO_CATEGORY = flip_dict(CATEGORY_TO_INGREDIENTS)
LONG_INGREDIENT_TO_CATEGORY = flip_dict(CATEGORY_TO_LONG_INGREDIENTS)