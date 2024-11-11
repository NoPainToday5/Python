def cipher(file, num):
    with open(file, "r") as file:
        text = file.read()

    ciphertext = ""

    for i in text:
        if(i == " " or i == "\n"):
            ciphertext += i
        else:
            if(i.isupper()):
                ciphertext += chr((ord(i) + num - 65) % 26 + 65)

            if(i.islower()):
                ciphertext += chr((ord(i) + num - 97) % 26 + 97)
    
    return ciphertext


def decypher(text, num, file, opt):

    decrypted_txt = ""

    for i in text:
        if(i == " " or i == "\n"):
            decrypted_txt += i
        else:
            if(i.isupper()):
                decrypted_txt += chr((ord(i) - num - 65) % 26 + 65)

            if(i.islower()):
                decrypted_txt += chr((ord(i) - num - 97) % 26 + 97)
    
    with open(file, opt) as file:
        if(opt == "w"):
            file.write(decrypted_txt)
        if(opt == "a"):
            file.write(decrypted_txt)
    
    return decrypted_txt

file_name = "./Files/cypher.txt"

encrypted = cipher(file_name, 23)
print(encrypted)

decrypted = decypher(encrypted, 23, file_name, "w")
print(decrypted)
