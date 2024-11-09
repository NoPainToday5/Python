from random import randint, choice
import string

def gen_char(password, characters):
    character = choice(characters) 
    if password == "":
        password += character
    else:
        while True:
            if character == password[i-1]:
                character = choice(characters) 
            else:
                break
    return character


password_length = randint(8,64) #length of a password according to standards
characters = string.ascii_letters +  string.digits + string.punctuation  # characters a-z, A-Z, 0-9, !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ 
password = "" # variable containing the password
uppercase_place = randint(0,password_length)
lowercase_place = randint(0,password_length)
digit_place = randint(0,password_length)
special_place = randint(0,password_length)

while True:
    if lowercase_place == uppercase_place or lowercase_place == special_place or lowercase_place == digit_place:
        lowercase_place = randint(0,password_length)
    elif special_place == uppercase_place or special_place == lowercase_place or special_place == digit_place:
        special_place = randint(0,password_length)
    elif digit_place == uppercase_place or digit_place == lowercase_place or digit_place == special_place:
        digit_place = randint(0,password_length)
    else:
        break


for i in range(password_length):
    if lowercase_place == i:
        password += gen_char(password, string.ascii_lowercase)
    elif uppercase_place == i:
        password += gen_char(password, string.ascii_uppercase)
    elif digit_place == i:
        password += gen_char(password, string.digits)
    elif special_place == i:
        password += gen_char(password, string.punctuation)
    else:
        password += gen_char(password, characters)


print(lowercase_place)
print(uppercase_place)
print(digit_place)
print(special_place)
print(password)
