print("This mini lab is a cooking measurement converter project. I will be working with lemonade. :)\n")

lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_cups = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input("How many servings does this make?\n"))

print(f"\nLemonade ingredients - yields {servings:.2f} servings")
print(f"{lemon_juice_cups:.2f} cup(s) lemon juice")
print(f"{water_cups:.2f} cup(s) water")
print(f"{agave_cups:.2f} cup(s) agave nectar")

print("\nHow many servings would you like to make?")

desired_servings = float(input())
scale_factor = desired_servings / servings

new_lemon_juice = lemon_juice_cups * scale_factor
new_water_cups = water_cups * scale_factor
new_agave_cups = agave_cups * scale_factor

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{new_lemon_juice:.2f} cup(s) lemon juice")
print(f"{new_water_cups:.2f} cup(s) water")
print(f"{new_agave_cups:.2f} cup(s) agave nectar")

cups_per_gallon = 16

lemon_juice_gallons = new_lemon_juice / cups_per_gallon
water_gallons = new_water_cups / cups_per_gallon
agave_gallons = new_agave_cups / cups_per_gallon

print(f"\nLemonade ingredients - yields {desired_servings:.2f} servings")
print(f"{lemon_juice_gallons:.2f} gallon(s) lemon juice")
print(f"{water_gallons:.2f} gallon(s) water")
print(f"{agave_gallons:.2f} gallon(s) agave nectar")