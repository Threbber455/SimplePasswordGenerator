# My 34
import random

randomInts = []

for i in range(0, 5):
    randomInts.append(chr(random.randint(48, 57)))  # 48 Being 0 in unicode, 57 being 9.

randomLetters = []

for i in range(0, 5):
    if i % 2 == 0:
        randomLetters.append(chr(random.randint(65, 90)).upper())  # 65 Being A in unicode, 90 being Z.
    else:
        randomLetters.append(chr(random.randint(65, 90)).lower())  # 65 Being A in unicode, 90 being Z.

randomCharacters = []

for i in range(0, 2):
    randomCharacters.append(chr(random.randint(33, 47)))  # 33 Being ! in unicode, 47 being /.

random.shuffle(randomInts)
random.shuffle(randomLetters)
random.shuffle(randomCharacters)

randomList = randomInts + randomLetters + randomCharacters
password = ""

random.shuffle(randomList)

for char in randomList:
    password += str(char)

print(password)

