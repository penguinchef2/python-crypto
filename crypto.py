########################### ENCRYPTION ####################################

def encrypt_text():
    with open("plain.txt") as file:
        plainText = file.read()
        stringList = list(plainText)  #converting the string to char first
        #print stringList
        tempList = [] #creating an empty list to store ascii values
        encryptedString = ""
        i = 0
        while i < 16: #looping through number of chars in my name
            tempList.append(ord(stringList[i])) #adding ascii values to temp list
            i+=1
        #print ("before encryption", tempList)
        key = 5 #the chosen key for this project
        i = 0
        while i < 16:
            tempList[i] = (tempList[i] + key) #shift 5 spaces forward
            i+=1
        chars  = [chr(n) for n in tempList]   #converting ascii values back to char 
        encryptedString = ''.join(chars) #joining chars back to string
        print ("Encrypted Text is: ", encryptedString)
        return tempList #returning list of ascii to decrypt

########################### DECRYPTION ####################################

def decrypt_text(inputKey, encryptedList):
    i = 0
    tempList = []
    while i < 16:
        encryptedList[i] = encryptedList[i] - inputKey #reversing encryption by moving 5 spaces back
        tempList.append(encryptedList[i])
        i+=1
    #print("decrypted number", encryptedList)
    chars  = [chr(n) for n in encryptedList] #converting ascii values to char
    encryptedString = ''.join(chars)
    print ("Your decrypted text is: ", encryptedString)


########################## MAIN #######################################

inputKey = 0

while inputKey != 1:
    encryptedList = encrypt_text()
    inputKey = int (input ("Enter your chosen key and 1 to exit : "))
    if inputKey == 5:
        print("Congratulations!")
        decrypt_text(inputKey, encryptedList)
        break
    if inputKey == 1:
        print("Thanks for guessing!")
        break
    else:
        print("Try again!")





