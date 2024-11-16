import os

def cipher(text, num):
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

def decypher(text, num):
    decrypted_txt = ""

    for i in text:
        if(i == " " or i == "\n"):
            decrypted_txt += i
        else:
            if(i.isupper()):
                decrypted_txt += chr((ord(i) - num - 65) % 26 + 65)

            if(i.islower()):
                decrypted_txt += chr((ord(i) - num - 97) % 26 + 97)
    
    return decrypted_txt

def filewriting(message):
    decision = input("Write or append a file? ")
    file_name = input("Input a file name with a path: ")

    if(decision == "write"):
        with open(file_name, "w") as file:
            file.write(message)
        file.close()
        print("Your new message: " + message)
            
    if(decision == "append"):
        with open(file_name, "a") as file:
            file.write("\n" + message)
        file.close()
        print("Your new message: " + message)
    
    return


ft = input("A file or a text? ").lower()
decision = input("Encrypt or decrypt? ").lower()
shift = int(input("By how many letters? "))

if(ft == "file"):
    while True:
        file_name = input("Input a file name with a path: ")
        if(os.path.isfile(file_name)):
            with open(file_name, "r") as file:
                text = file.read()
            file.close()
            break
        else:
            print("The file does not exist. Enter a valid file.")

    if (decision == "encrypt"):
        encrypted = cipher(text, shift)
        ft = input("Write it to a file? ").lower()

        if(ft == "yes"):
            filewriting(encrypted)
        
        if(ft == "no"):
            print("Your new message: " + encrypted)

        

    if (decision == "decrypt"):
        decrypted = decypher(text, shift)
        ft = input("Write it to a file? ").lower()

        if(ft == "yes"):
            filewriting(decrypted)
        
        if(ft == "no"):
            print("Your new message: " + decrypted)
    
    
    

if(ft == "text"):
    text = input("Input text: ")

    if (decision == "encrypt"):
        encrypted = cipher(text, shift)
        ft = input("Write it to a file? ").lower()

        if(ft == "yes"):
            filewriting(encrypted)
        
        if(ft == "no"):
            print("Your new message: " + encrypted)

    if (decision == "decrypt"):
        decrypted = decypher(text, shift)
        ft = input("Write it to a file? ").lower()

        if(ft == "yes"):
            filewriting(decrypted)
        
        if(ft == "no"):
            print("Your new message: " + decrypted)