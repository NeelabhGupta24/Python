import random
#creating list
symbols = []
letters = []
numbers = []
#adding symbols in list
for ascii in range(33,48):
    symbols.append(chr(ascii))
for ascii in range(58,65):
    symbols.append(chr(ascii))
#adding numbers in list
for ascii in range(48,58):
    numbers.append(chr(ascii))
#adding letters in list
for ascii in range(65,91):
    letters.append(chr(ascii))
for ascii in range(97,123):
    letters.append(chr(ascii))
number_of_symbols = 0
number_of_letters = 0
number_of_digits = 0
while True:
    flag = False
    number_of_symbols = int(input("Enter The number of symbols you want in your password :"))
    number_of_letters = int(input("Enter The number of letters you want in your password :"))
    number_of_digits = int(input("Enter The number of digits you want in your password :"))
    length = number_of_digits+number_of_letters+number_of_symbols
    while True:
        approval = input(f"Total length of your password is {length}, Do you want to proceed (Y/N) :")
        if(approval.lower()=="y"):
            flag = True
            break
        elif(approval.lower()=="n"):
            flag = False
            break
        else:
            print("Please enter Y or N")
    if flag:
        break
password = []
for symbol in range(number_of_symbols):
    password.append(random.choice(symbols))
for digit in range(number_of_digits):
    password.append(random.choice(numbers))
for letter in range(number_of_letters):
    password.append(random.choice(letters))
random.shuffle(password)
final_password = ""
for char in password:
    final_password+=char
print(f"Your password can be {final_password}")