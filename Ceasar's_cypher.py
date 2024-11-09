def cipher(file, num):
    with open(file, "r") as file:
        text = file.read()

    ciphertext = ""
    
    for i in text:
        if(i == " " or i == "\n"):
            continue
        else:
            if(ord(i) >= 65 and ord(i) <= 90):
                if((ord(i)+num) > 90):
                    ciphertext += chr( ((ord(i) + num) % 90) + 65 )
                else:
                    ciphertext += chr( ((ord(i) + num) % 90))


    return

file_name = "./Files/cypher.txt"

print(chr( ((ord("Z") + 0) - 90) + 65))


