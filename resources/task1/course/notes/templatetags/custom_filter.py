from django import template
from django.urls import reverse
from django.utils.html import format_html
import re

register = template.Library()

@register.filter(name='escape_angle_brackets')
def escape_angle_brackets(value):
    
    return re.sub(r'&gt; and &lt;', '< and >', value)


@register.filter(name='linkable_section')
def linkable_section(section_name):
    
    url = reverse('notes:by_section', args=[section_name])
    
    return format_html('<a href="{}">{}</a>', url, section_name)


