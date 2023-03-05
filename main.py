import random
import string
from random import choice
from string import printable
status = False
score = int(input("Задайте длинну пароля в диапазоне от 7 до 20 (число): "))
while score>20 or score < 7:
  print("К сожалению, пароль не входит в диапазон возможных значений. Попробуйте еще раз!")
  score = int(input("Какова длинна пароля?"))
else:
 while status == False :
   password = ''.join([choice(list(printable)) for item in range(0, score)])
   password2 = password.replace(" ", choice(list(printable)))
   print(password2)
   likedislike = input("Вам понравился пароль?  (да/нет): ")
   if likedislike == "да":
    break
