with open('input.txt') as f:
    input_data = f.read().strip()

def switch_case(c):
    if c.isupper():
        return c.lower()
    else:
        return c.upper()

def run_reactions(polymer):
    for i in range(len(polymer)):
        if i + 1 == len(polymer):
            break
        if polymer[i] == switch_case(polymer[i + 1]):
            polymer = polymer[0:i] + polymer[i+2:]
            return polymer
    return polymer

old_polymer = input_data
while True:
    polymer = run_reactions(old_polymer)
    if old_polymer == polymer:
        print len(polymer)
        break
    old_polymer = polymer
