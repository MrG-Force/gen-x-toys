from django import template

register = template.Library()

@register.inclusion_tag('cart/form_field.html')
def form_field(field, wrapper_classes="", error_message_prefix="* Please enter your "):
     return {'field': field, 'wrapper_classes': wrapper_classes, 'error_message_prefix': error_message_prefix}