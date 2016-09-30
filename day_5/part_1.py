def has_three_vowels(string):
    return len(filter(lambda c: c in 'aeiou', string)) >= 3


def has_repeated_letter(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        if letter * 2 in string:
            return True
    return False


def contains_substrings(string):
    substrings = ['ab', 'cd', 'pq', 'xy']
    for substring in substrings:
        if substring in string:
            return True
    return False


def is_nice(string):
    return has_three_vowels(string) and has_repeated_letter(string) and not contains_substrings(string)


strings = []
with open('input.txt') as f:
    for line in f:
        strings.append(line.strip())
strings_are_nice = [is_nice(s) for s in strings]
print sum([bool(s) for s in strings_are_nice])
