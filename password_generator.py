import random

letters = "abcdefghijklmnopqrstuvwxyz"
lettersBig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()-_+"

all = letters + lettersBig + numbers + symbols
length = 10
password=open("pass.txt", "w")
password.write("".join(random.sample(all, length)))
