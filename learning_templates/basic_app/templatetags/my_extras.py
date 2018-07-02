#create this file to put in the custom filters.

from django import template

register = template.Library()

# @register.filter(name='cut')   See note below about using decorators to register.
def cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

#then rester this. here the cut is the name you want to call the function. then pass in the function itself.

register.filter('cut', cut)

#Above is another way to register custom filters by using decorators and it looks cleaner.
#above since the function is passed in to another function we can just use a decorator. 
