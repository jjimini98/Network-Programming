number = sorted(list(map(int, input().split(" "))))

big = number[1]
small = number[0]
while True:
    ingyeo = big%small
    big = small
    small = ingyeo
    if small == 0:
        print("최대공약수는 바로" , big)
        break
