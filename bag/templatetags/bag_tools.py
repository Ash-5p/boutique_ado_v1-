from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def cala_subtotal(price, quanitity):
    return price * quanitity
