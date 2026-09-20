#Lists of alphabet
lower_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']

#Functions
def encrypt(content,shift):
    translation = ""
    for letter in content:
        if letter in lower_alphabets:
            index = lower_alphabets.index(letter)
            if (index+shift)>25:
                index += shift-26
            else:
                index += shift
            translation+=lower_alphabets[index]
        elif letter in upper_alphabets:
            index = upper_alphabets.index(letter)
            if (index+shift)>25: #adresses index range to be within limit
                index += shift-26
            else:
                index += shift
            translation+=upper_alphabets[index]
        else:
            translation+=letter
    print(translation)
        
def decrypt(content,shift):
    translation = ""
    try:
        for letter in content:
            if letter in lower_alphabets:
                index = lower_alphabets.index(letter)
                if (index-shift)<0: #adresses index range to be within limit
                    index +=26
                    index -= shift
                else:
                    index -= shift
                translation+=lower_alphabets[index]
            elif letter in upper_alphabets:
                index = upper_alphabets.index(letter)
                if (index-shift)<0:
                    index += 26
                    index -= shift
                else:
                    index -= shift
                translation+=upper_alphabets[index]
            else:
                translation+=letter
    except IndexError:
        print(index)
    print(translation)

while True:
    choice = input("Enter E for Encryption, D for decryption :")
    if choice.lower() == 'd':
        user_input = input("Enter Content to be Decrypted :")
        shift_input = int(input("Enter Shift :"))
        decrypt(content=user_input,shift=shift_input)
        break
    elif choice.lower() == 'e':
        user_input = input("Enter Content to be Encrypted :")
        shift_input = int(input("Enter Shift :"))
        encrypt(content=user_input,shift=shift_input)
        break
    else:
        print("Please enter a valid choice")