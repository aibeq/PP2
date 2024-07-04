import re

def camel_to_snake(string):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', string).lower()

# Example
print(camel_to_snake('KakyuEsheDozy?'))
