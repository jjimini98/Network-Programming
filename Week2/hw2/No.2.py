# 두 수의 최대 공약수는 두 수를 나누어 떨어지는 가장 큰 수이다.
# 예를 들어 (16, 24)의 최대 공약수는 8이다. 두 수를 입력 받아
# 다음 알고리즘에 의해 최대 공약수를 구하는 프로그램을
# 작성하라.
# ● 큰 수를 작은 수로 나눈 나머지를 구하라
# ● 큰 수를 작은 수로 대체하고 작은 수는 나머지로 대체하라
# ● 작은 수가 0이 될 때까지 이 과정을 반목하라. 마지막 큰 수가 최대 공약수이다.


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
