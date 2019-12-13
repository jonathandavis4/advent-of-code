from decimal import Decimal, ROUND_DOWN

def get_fuel_required(mass):
    return (mass / 3).quantize(1, rounding=ROUND_DOWN) - 2

with open('input.txt') as f:
    masses = f.read().strip().split('\n')

print sum(map(get_fuel_required, map(Decimal, masses)))
