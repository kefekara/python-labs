import random
code = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzun = int(input("uzunluk gir"))

parola = ""

for _ in range (uzun):
    parola += random.choice(code)
print (parola)