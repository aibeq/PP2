import re

def insert_spaces_between_capitals(string):
    pattern = r'(?=[A-Z])'
    return ' '.join(re.split(pattern, string))

# Example
print(insert_spaces_between_capitals('BestString')) 
