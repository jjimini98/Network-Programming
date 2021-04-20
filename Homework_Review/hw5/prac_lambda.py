msg = input()

msg = msg.split(" ")
fi = int(msg[0])
cal = msg[1]
se = int(msg[2])

if cal == "+":
    print((lambda x, y: x + y)(fi, se))
elif cal == "-":
        print((lambda x, y : x-y)(fi,se))
elif cal == "*":
    print((lambda x, y : x*y)(fi,se))
elif cal == "/":
    print('%.1f' %(lambda x,y : x/y)(fi,se))