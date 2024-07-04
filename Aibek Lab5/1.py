import re

def match_a_followed_by_zero_or_more_b(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

# Example
print(match_a_followed_by_zero_or_more_b('ab'))
print(match_a_followed_by_zero_or_more_b('a'))   
print(match_a_followed_by_zero_or_more_b('b'))   
