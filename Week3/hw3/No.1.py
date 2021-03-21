#p.67

days = {'January' : 31, 'February' : 28 , 'March'  : 31 , 'April' : 30 , 'May' : 31 , 'June' : 30 , 'July' : 31,
        'August'  : 31 , 'September' : 30 , 'October' : 31 , 'November' : 30 , 'December' : 31}


#1. 사용자가 월을 입력하면 해당 월의 일수를 출력하라.
print("1번 : 월을 입력하면 해당 월의 일수를 알려드립니다. (ex. January)")
user = input(">>") #월 입력

if user in days:
    print(days[user])


#2. 알파벳 순서로 모든 월을 출력하라.
print("2번 : 알파벳 순서대로 정렬된 모든 월을 출력합니다.")
print(sorted(list(days.keys())))

#3. 일수가 31일 월을 모두 출력하라.
print("3번 : 일수가 31일인 모든 월을 출력합니다.")
for x in days.items(): #x값에는 튜플이 들어감 ex. ('January' ,31)
    if x[1] == 31:
       print(x[0])

#4. 월의 일수를 기준으로 오름차 순으로 key-value 쌍을 출력하라.
print("4번 : 월의 일수를 기준으로 오름차순으로 정렬된 key-value쌍을 출력합니다.")
li = list(days.items())
li.sort(key=lambda x: x[1])
for i in li:
    print(i[0],i[1])


#5. 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.
print("5번 : 월의 3자리만 입력하면 월의 일수를 알려드립니다. (ex.Jan,Feb)")
user = input(">>")

for x in days.items():
    if user in x[0]:
        print(x[1])
