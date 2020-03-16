{% for meal in meals %}
{{ meal.name }}{% for ingredient in meal.ingredients %}
    - {{ ingredient }}{% endfor %}
{% endfor %}