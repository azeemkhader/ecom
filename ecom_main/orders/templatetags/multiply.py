from django import template

register=template.Library()


@register.simple_tag(name='multiply')
def multiply(price,quantity):
   
   return price * quantity