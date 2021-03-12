import sys

word = sys.stdin.readline()

for x in range(0,len(word)):
    if word[x] =="a":
        print(word[x])
    else:
        print(word[x], end='')
