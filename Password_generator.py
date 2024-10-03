import random
import string

password_length = random.randint(8,64) #length of a password according to standards
characters = string.ascii_letters +  string.digits + string.punctuation  # characters a-z, A-Z, 0-9, !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ 
password = "" # variable containing the password

for i in range(password_length):
    character = characters[random.randint(0,len(characters)-1)]
    if password == "":
        password += character
    else:
        while True:
            if character == password[i-1]:
                character = characters[random.randint(0,len(characters)-1)]
            else:
                break
        password += character

print(password)
