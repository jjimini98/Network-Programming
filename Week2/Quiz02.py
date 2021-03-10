lis = ['이지희','장보현','이가현']

print(lis.insert(2,"유지민"))
print(lis.append("이지윤"))


num_lis = [1,2,3]
num_lis[1]=17
print(num_lis)
print(num_lis.append([4,5,6]))
print(num_lis.pop(0))
num_lis= sorted(num_lis)
print(num_lis)
print(num_lis.sort(reverse=True))
num_lis[3]=25
print(num_lis)