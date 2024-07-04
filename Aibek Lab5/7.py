import re

def split_at_uppercase(string):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, string)

# Example
print(split_at_uppercase('AibekIsTheBestAkylStudent'))  
