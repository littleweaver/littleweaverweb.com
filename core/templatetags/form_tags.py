from django import template
from django.forms.widgets import CheckboxInput


register = template.Library()


@register.filter
def get_value(bound_field):
    return bound_field.value()


@register.filter
def is_checkbox(bound_field):
    return isinstance(bound_field.field.widget, CheckboxInput)


@register.filter
def id(bound_field):
    widget = bound_field.field.widget
    for_id = widget.attrs.get('id') or bound_field.auto_id
    if for_id:
        for_id = widget.id_for_label(for_id)
    return for_id
