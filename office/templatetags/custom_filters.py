# app/templatetags/custom_filters.py
from django import template
import json

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary.get(key)


@register.filter
def json_to_dict(value):
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return {}
    

@register.filter
def dict_to_json(value):
    return json.dumps(value)