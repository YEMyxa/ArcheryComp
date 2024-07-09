from django import template
register = template.Library()

@register.simple_tag(takes_context=True,name='my_foo')
def foo(context, a,b):
    return f"in foo func, args: {a=}, {b=}"