import random
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
q1 = int(input("qual será o comprimento da sua senha? "))
senha = ""


for i in range(q1):
    senha+= random.choice(elementos)

print(senha)

