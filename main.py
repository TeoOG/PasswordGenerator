#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letter_number_list = [None] * nr_letters
random_symbol_number_list = [None] * nr_symbols  
random_numbers_number_list = [None] * nr_numbers

letter_pass = [None] * nr_letters
symbol_pass = [None] * nr_symbols  
number_pass = [None] * nr_numbers

# print(type(random_letter_number_list))

# Generate random letters
for n in range(0, nr_letters):
    random_letter_number_list[n] = random.randint(0, len(letters) - 1) # index
    # print(letters[random_letter_number_list[n]])
    letter_pass[n] = letters[random_letter_number_list[n]]

# Generate random symbols
for n in range(0, nr_symbols):
    random_symbol_number_list[n] = random.randint(0, len(symbols) - 1)
    # print(symbols[random_symbol_number_list[n]])
    symbol_pass[n] = symbols[random_symbol_number_list[n]]

# Generate random numbers
for n in range(0, nr_numbers):
  random_numbers_number_list[n] = random.randint(0,len(numbers) - 1)
  # print(numbers[random_numbers_number_list[n]])
  number_pass[n] = numbers[random_numbers_number_list[n]]

# print(random_letter_number_list)
# print(random_symbol_number_list)
# print(random_numbers_number_list)

# print(letter_pass)
# print(symbol_pass)
# print(number_pass)
password = letter_pass + symbol_pass + number_pass
# print(password)
print(f"your password is {''.join(password)}")
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
randomised_password = password

# for n in randomised_password:
#   x = random.randint(0, len(randomised_password) - 1)
#   element = randomised_password.pop(x)
#   randomised_password.append(element)


for i in range(len(randomised_password)-1,0,-1):
    j = random.randint(0, i) #selecting a random item's index
    randomised_password[i],randomised_password[j] = randomised_password[j],randomised_password[i] #swapping the two items
# print("The shuffled list is: ",randomised_password)


# print(randomised_password)
print(f"your password is {''.join(randomised_password)}")
