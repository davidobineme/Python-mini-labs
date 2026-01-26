user_int = int(input("Enter integer (32 - 126):\n"))

user_flt = float(input("Enter float:\n"))

user_chr = (input("Enter character:\n"))

user_str = (input("Enter string:\n"))

print(str(user_int) + " " + str(user_flt) + " " + user_chr + " " + user_str)

print(user_str + " " + user_chr + " " + str(user_flt) + " " + str(user_int))

print(str(user_int) + " converted to a character is " +chr(user_int))