from django import template

register = template.Library()

# returns the first three scentences of a given text
@register.filter(name="shorten")
def shorten(value):
    tempVal = value.split(" ")
    retVal = ""
    for c in tempVal:
        retVal += f"{c} "
        if len(retVal) > 600:
            retVal += " ..."
            break
    return retVal
