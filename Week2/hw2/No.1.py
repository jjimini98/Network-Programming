# ● 플레이어가 처음에 $50을 가지고 있다. 동전을 한 번 던져서 앞면(1) 또는
# 뒷면(2)이 나온다. 맞추면 $9을 따고 틀리면 $10을 잃는다. 플레이어가 돈을 모두
# 잃거나 $100이 되면 게임이 종료된다.
# ● 동전을 던져서 나오는 수는 다음 문장을 이용하라.
# from random import randint
# coin = randint(1,2) #1 또는 2를 임의로 발생


from random import randint
import sys

player_answer = map(int, sys.stdin.readline())
player_coin  = 50
coin = randint(1,2)
while player_coin == 100 or player_coin == 0 :
   if player_answer == coin :
      player_coin += 9
      print("your coin is", player_coin)

   else:
      player_coin -= 10 
      print("your coin is", player_coin)
