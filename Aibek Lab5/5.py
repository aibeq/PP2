import re

def find_uppercase_followed_by_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

# Example
print(find_uppercase_followed_by_lowercase('Soomething_IsHere But wHy'))  