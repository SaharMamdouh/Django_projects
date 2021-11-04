from django.template import Library
register=Library()
@register.filter
def cut(text):

    # get slice object to slice Python
    sliced_text = slice(6)
    return text[:12]


