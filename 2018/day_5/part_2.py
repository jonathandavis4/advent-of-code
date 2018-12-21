from string import ascii_lowercase

with open('input.txt') as f:
    input_data = f.read().strip()

def switch_case(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()

def run_reactions(old_polymer):
    polymer = None
    while old_polymer != polymer:
        if polymer is None:
            polymer = old_polymer
        old_polymer = polymer
        for letter in ascii_lowercase:
            polymer = polymer.replace('{}{}'.format(letter.lower(), letter.upper()), '')
            polymer = polymer.replace('{}{}'.format(letter.upper(), letter.lower()), '')
    return polymer

results = []
for letter in ascii_lowercase:
    old_polymer = input_data.replace(letter, '').replace(letter.upper(), '')
    polymer = run_reactions(old_polymer)
    results.append([letter, len(polymer)])
print min(results, key=lambda x: x[1])[1]
