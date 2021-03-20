
import random
#Password Generator


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password=""
# Order not randomised:

for item in range(0,nr_letters):
  rletter=random.randint(0,51)
  password=letters[rletter]+password
for item in range(0,nr_symbols):
  rnum=random.randint(0,9)
  password=symbols[rnum]+password
for item in range(0,nr_numbers):
  rsymbol=random.randint(0,8)
  password+=numbers[rsymbol]
# print(password)



#Order of characters randomised:

l = list(password)
random.shuffle(l)
result = ''.join(l)
print(result)
