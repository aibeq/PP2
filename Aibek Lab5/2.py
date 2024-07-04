import re

def find_lowercase_sequences_with_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

print(find_lowercase_sequences_with_underscore( 'Example_of something_now'))