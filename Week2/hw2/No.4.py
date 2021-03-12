for x in range(1,1001):
    sum = 0
    for t in str(x):
        sum+=int(t)
    print(x,"의 자릿수의 합은",sum)
