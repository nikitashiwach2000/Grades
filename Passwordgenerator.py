import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# nr_letters = int(input("How many letters would you add in password: "))
# password_len = int(input("enter the length of password: "))
nr_letters = random.randint(6,12)
# nr_symbols = int(input("How many symbols would you add: "))
nr_symbols = random.randint(6,12)

# nr_numbers = int(input("How many numbers would you add: "))
nr_numbers = random.randint(6,12)


password = ""
for i in range(0,nr_letters+1):
    rand_letters = random.choice(letters)
    password= password+rand_letters

for i in range(0,nr_symbols):
    rand_symbols = random.choice(symbols)
    password = password+rand_symbols

for i in range(0,nr_numbers):
    rand_num = random.choice(numbers)
    password = password+rand_num
print(password)

# ''.join(random.sample(password,len(password)))
# print(password)

# for i in range(0,password_len):
password_list =[]
for i in range(0,nr_letters+1):
    password_list.append(random.choice(letters))

for i in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
        
for i in range(0,nr_numbers):
    password_list.append(random.choice(numbers))

        
    random.shuffle(password_list)

for password in password_list:
    print(password,end="")
print()