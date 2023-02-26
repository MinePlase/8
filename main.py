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
                    likedislike = input("Вам понравился пароль?  (да/нет): ")
                    if likedislike == "да":
                    print("Спасибо за использование")
                        break
