import re

def snake_to_camel(string):
    components = string.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Example
print(snake_to_camel('Why_am_I_typing_this'))  
