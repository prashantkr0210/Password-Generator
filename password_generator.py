#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the MyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#When Order of characters is not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""  

for i in range(0, nr_letters):
  random_number_letters=random.randint(0,len(letters)-1)   
  password = password + letters[random_number_letters]

for j in range(0, nr_symbols):
  random_number_symbols=random.randint(0,len(symbols)-1)  
  password = password + symbols[random_number_symbols]

for k in range(0, nr_numbers):
  random_number_numbers=random.randint(0,len(numbers)-1) 
  password = password + numbers[random_number_numbers] 

print(f"\nYour password without randomised character is :  {password}")
  
#When Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []  

for c in range(0, nr_letters):
    password_list.append(random.choice(letters))    
for c in range(0, nr_symbols):
    password_list += random.choice(symbols)
for c in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)    

password1 = ""  # creating an empty string..will convert above list into string

for d in range(0, len(password_list)):   
    password1 += password_list[d]        

print(f"\nYour password with randomised character (More Secure) is : {password1}")