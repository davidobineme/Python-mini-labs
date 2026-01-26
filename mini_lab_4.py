import math

people_per_pizza = 12 / 2

number_people = int(input())

print("People: " + str(number_people))

number_pizza = math.ceil(number_people / people_per_pizza)

print(f"Pizza(s): {number_pizza}")

total = number_pizza * 14.95

print(f"Cost for {number_pizza} pizza(s): ${total:.2f}")