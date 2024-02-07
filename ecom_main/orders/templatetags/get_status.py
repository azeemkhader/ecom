from django import template

register=template.Library()


@register.simple_tag(name='get_status')

def get_status(status):
   
   status=status-1
   status_array=['CONFIRMED','PROCESSING', 'DELIVERED', 'REJECTED' ]

   return status_array[status]

   