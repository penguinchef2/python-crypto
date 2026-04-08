########################### ENCRYPTION ####################################

def encrypt_text():
    with open("plain.txt") as file:
        plainText = file.read()
        plainText = plainText.encode(encoding = "ascii") #converting to ascii values
        stringList = list(plainText) #converting to list  of ascii
        #print ("before encryption", stringList)
        key = 5 #the chosen key for this project
        i = 0
        while i < 16:
            stringList[i] = (stringList[i] + key) #shift 5 spaces forward
            i+=1
        #print("encrypted number", stringList)
        i = 0
        chars = []
        while i<16:
            chars.append(chr(stringList[i])) #converting each ascii number to char
            i+=1
        encryptedString = ''.join(chars) #joining chars back to string
        print ("Encrypted Text is: ", encryptedString)
        return encryptedString #returning list of ascii to decrypt

########################### DECRYPTION ####################################

def decrypt_text(inputKey, encryptedList):
    encryptedList = encryptedList.encode( encoding = "ascii")
    encryptedChar = list(encryptedList)
    j = 0
    while j < 16:
        encryptedChar[j] = encryptedChar[j] - inputKey #reversing encryption by moving 5 spaces back
        j+=1
    #print("decrypted number", encryptedChar)
    chars = []
    i = 0
    while i<16:
        chars.append(chr(encryptedChar[i]))
        i+=1
    encryptedString = ''.join(chars)
    print ("Your decrypted text is: ", encryptedString)


########################## MAIN #######################################

inputKey = 0

while inputKey != 1:
    encryptedString = encrypt_text()
    inputKey = int (input ("Enter your chosen key and 1 to exit : "))
    if inputKey == 5:
        print("Congratulations!")
        decrypt_text(inputKey, encryptedString)
        break
    if inputKey == 1:
        print("Thanks for guessing!")
        break
    else:
        print("Try again!")





