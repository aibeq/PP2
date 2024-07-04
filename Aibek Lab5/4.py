import re

def replace_space_comma_dot_with_colon(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

# Example
print(replace_space_comma_dot_with_colon('Another Example Is HERe'))
