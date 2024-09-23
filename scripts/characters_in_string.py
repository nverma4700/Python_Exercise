def char_in_strings(text):
    upper_list = []
    lower_list = []
    other = []
    for char in text:
        if char == " " or char == "\n":
             continue
        elif char.isupper():
            upper_list.append(char)
        elif char.islower():
            lower_list.append(char)
        else:
            other.append(char)
    category = {
        'Uppercase': ''.join(upper_list),
        'Lowercase': ''.join(lower_list),
        'Other': ''.join(other)
    }
    return category

if __name__ == "__main__":
    text = '''WzY7sM4JcYHJYgEvQCmoSjWCrcMApgD 
    r5tHNIT1nWYptFjjGytaiHZtQw163il 
    sJGNFrHgV9PcW4LDDJOcHJRskS8WqRO 
    3PhG4ViLjqN550urrO62etnIgusTLGK 
    cEFvnFGEflIJJ5mecC28NkPUYA2o5pX'''
    char_string = char_in_strings(text)
    for k, v in char_string.items():
        print(f'{k}: {v}')