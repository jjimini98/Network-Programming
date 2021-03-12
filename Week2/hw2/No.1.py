from random import randint

player_coin = 50

while True:
   coin = randint(1, 2)
   print("-------------------------------------------")
   player_answer = int(input("select coin 1 or 2:"))

   if player_answer == coin :
      player_coin += 9
      print("your coin is", player_coin)

      if player_coin >= 100:
         print("player win!")
         break

      elif player_coin <= 0:
         print("player lose :(")
         break

   else:
      player_coin -= 10 
      print("your coin is", player_coin)

      if player_coin >= 100 :
         print("==================result===================")
         print("player win! :)")
         break

      elif player_coin <=0:
         print("==================result===================")
         print("player lose :(")
         break
