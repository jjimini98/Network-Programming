lst = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']

#A.
lst.append('!')
print(lst)

#B.
del lst[4]
print(lst)

#C.
lst.insert(4,'a')
print(lst)

#D.
new_lst=''.join(lst)
print(new_lst)

#E.
print(sorted(lst,reverse=True))