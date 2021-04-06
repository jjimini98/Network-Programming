from socket import *
import struct

# def calculator(sentence):
#     sentence= sentence.split(" ")
#
#     if sentence[1] == "+":
#         return int(sentence[0]) + int(sentence[2])
#
#     elif sentence[1] == "-":
#         return int(sentence[0]) - int(sentence[2])
#
#     elif sentence[1] == "*":
#         return int(sentence[0]) * int(sentence[2])
#
#     elif sentence[1] == "/":
#         return  format(int(sentence[0]) / int(sentence[2]), ".1f")
#
#
# print(calculator("25 / 25"))
# print(calculator("27 / 2 "))


result = 3 + 5
packed_float = struct.pack('f', result)
print(packed_float)

unpack = struct.unpack('f',packed_float)
print(unpack)