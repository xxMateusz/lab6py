import random
import string
import random
import string

def passGen(length, minNum, minLett):
    alf = string.ascii_letters
    num = ''.join(str(i) for i in range(10))
    evry = alf + num
    li = [char for char in evry]

    while True:
        haslo = []
        for _ in range(length):
            haslo.append(random.choice(li))
        count = sum(1 for char in haslo if char.isdigit()) # Liczymy cyfry
        count_letter = sum(1 for char in haslo if char.isalpha()) # Liczymy litery
        if count >= minNum and count_letter >= minLett:
            yield ''.join(haslo)

# Testowanie generatora
gen = passGen(8, 2, 2)
for _ in range(5): # Generujemy 5 haseł
    print(next(gen))