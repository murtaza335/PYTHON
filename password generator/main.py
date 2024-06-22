# generate a random and secure password of length 12 
import random
alphabets = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
special_characters = (
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '~'
)
password = []
for i in range(3):
    password.append(random.choice(alphabets))
for i in range(3,6):
    password.append(random.choice(numbers))
for i in range(6,9):
    password.append(random.choice(special_characters))
for i in range(9,12):
    rand = random.choice(alphabets)
    password.append(rand.upper())
for i in range(12,15):
    password.append(random.choice(numbers))
random.shuffle(password)
# print password
for i in password:
    print(i,end="")
