from socket import *


def calculator(sentence):
    sentence= sentence.split(" ")

    if sentence[1] == "+":
        return int(sentence[0]) + int(sentence[2])

    elif sentence[1] == "-":
        return int(sentence[0]) - int(sentence[2])

    elif sentence[1] == "*":
        return int(sentence[0]) * int(sentence[2])

    elif sentence[1] == "/":
        return  format(int(sentence[0]) / int(sentence[2]), ".1f")


print(calculator("25 / 25"))
print(calculator("27 / 2 "))