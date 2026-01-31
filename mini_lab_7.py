print("This is a mini lab using specific questions and answers to generate passwords for the user.\nFirst we input color, pet name and favorite number.\n")

color = input()
pet_name = input()
favorite_number = input()

print(f"You entered: {color} {pet_name} {favorite_number}\n")

first_pass = color + "_" + pet_name
second_pass = favorite_number + color + favorite_number

print(f"First password: {first_pass}")
print(f"Second password: {second_pass}\n")

num_chr_first = len(first_pass)
num_chr_second = len(second_pass)

print(f"Number of characters in {first_pass}: {num_chr_first}")
print(f"Number of characters in {second_pass}: {num_chr_second}")