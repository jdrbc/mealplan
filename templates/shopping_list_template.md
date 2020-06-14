{% for category in categories %}
# {{ category }}{% for ingredient in category_to_ingredients.get(category) %}

- {{ ingredient }}{% endfor %}
{% endfor %}