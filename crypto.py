########################### ENCRYPTION ####################################

def encrypt_text():
    with open("plain.txt") as file:
        plainText = file.read()
        stringList = list(plainText)  #converting the string to char first
        #print stringList
        encryptedString = ""
        i = 0
        while i < 16: #looping through number of chars in my name
            stringList[i] = (ord(stringList[i])) #adding ascii values to temp list
            i+=1
        print ("before encryption", stringList)
        key = 5 #the chosen key for this project
        i = 0
        while i < 16:
            stringList[i] = (stringList[i] + key) #shift 5 spaces forward
            i+=1
        chars  = [chr(n) for n in stringList]   #converting ascii values back to char 
        encryptedString = ''.join(chars) #joining chars back to string
        print ("Encrypted Text is: ", encryptedString)
        return encryptedString #returning list of ascii to decrypt

########################### DECRYPTION ####################################

def decrypt_text(inputKey, encryptedList):
    i = 0
    encryptedChar = list(encryptedList)
    while i < 16:
        encryptedChar[i] = (ord(encryptedChar[i]))
        i+=1
    j = 0
    while j < 16:
        encryptedChar[j] = encryptedChar[j] - inputKey #reversing encryption by moving 5 spaces back
        j+=1
    print("decrypted number", encryptedChar)
    chars  = [chr(n) for n in encryptedChar] #converting ascii values to char
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





