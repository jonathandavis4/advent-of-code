from decimal import Decimal, ROUND_DOWN

def get_fuel_required(mass):
    return (mass / 3).quantize(1, rounding=ROUND_DOWN) - 2

with open('input.txt') as f:
    masses = f.read().strip().split('\n')

total_fuel = 0
for mass in masses:
    this_fuel = 0
    mass = Decimal(mass)
    fuel = get_fuel_required(mass)
    this_fuel += fuel
    while fuel > 0:
        fuel = get_fuel_required(fuel)
        if fuel > 0:
            this_fuel += fuel
    total_fuel += this_fuel

print total_fuel