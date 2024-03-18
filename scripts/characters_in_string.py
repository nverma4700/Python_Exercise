import string


def char_in_strings(text):
    '''
    Iterate through the text and returns all uniques uppercase, 
    lowercase, and special/number charatcter.
    '''
    catagories = {}
    for char in text: 
        if char != ' ':  # ignores the white space
            if char in string.ascii_lowercase:
                key = 'lower_case'
            elif char in string.ascii_uppercase:
                key = 'upper_case'
            else:
                key = 'others'
            
            catagories.setdefault(key, set()).add(char) # initiates with the empty set and keep adding char to set
    for cat in catagories:
        print(f"{cat}: ", ''.join(catagories[cat]))

## Testing: 
text = '''WzY7sM4JcYHJYgEvQCmoSjWCrcMApgD 
r5tHNIT1nWYptFjjGytaiHZtQw163il 
sJGNFrHgV9PcW4LDDJOcHJRskS8WqRO 
3PhG4ViLjqN550urrO62etnIgusTLGK 
cEFvnFGEflIJJ5mecC28NkPUYA2o5pX'''
char_in_strings(text)