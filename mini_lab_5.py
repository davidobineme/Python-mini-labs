import math

print("HOLA MI AMIGO(A)!")
print("This mini lab is focused on learning how to use the square root function in python. Give me a number. ;)")

print(" ")

value1 = float(input())
value2 = float(math.sqrt(value1))

print(f"Square root of {value1:.2f} = {value2:.2f}")
print(" ")
print("Now that we are done with decimals (floats), now we will move on to whole numbers (integers).")

value3 = int(input())
value4 = int(math.sqrt(value3))

print(f"Square root of {value3} = {value4}")

print(" ")

print("Fun right? Bet! Now that we are done with that lets try mixing them both. The next number should be written as a whole number and will be converted to two decimal places.")

value5 = int(input())
value6 = float(math.sqrt(value5))

print(f"Square root of {value5:.1f} = {value6:.2f}")

print(" ")

print("Ok bye for now. May I ask your name?")

print(" ")

name1 = input()
print("Nice to meet you " +str(name1) + "!. Call me Big Daddy Dave. Thank you for your time.")