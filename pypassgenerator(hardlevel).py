import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','10',]
characters=['!','@','#','$','%','^','&','&']
print("welcome to the pypass generator")
n_letters=int(input("how many letters do you want in your password\n"))
n_numbers=int(input("how many numbers do you want in your password\n"))
n_charcters=int(input("how many characters do you want in your password\n"))
password_list =[]
for char in range(1,n_letters+1):
    random_char=random.choice(letters)
    password_list+=random_char
print(random_char)
for num in range(1,n_numbers+1):
    random_num=random.choice(numbers)
    password_list+=random_num
print(random_num)
for symbol in range(1,n_charcters+1):
    random_symbol=random.choice(characters)
    password_list+=random_symbol
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password+=char
print(password)