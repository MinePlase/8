import random
import string
from random import choice
from string import printable
status = False
score = int(input("Какова длинна пароля?"))
while score>20 or score < 7:
    print("Пароль не подходит! Попробуй еще раз!")
    score = int(input("Какова длинна пароля?"))
else:
    while status == False :
                answer=input("Хотите получить пароль? (yes/no)  ")
                if answer == "no":
                    break
                elif answer == "yes" :
                    password = ''.join([choice(list(printable)) for item in range(0, score)])
                    password2 = password.replace(" ", "")
                    print(password2)
                    status == True
                    likedislike = input("Вам понравился пароль?  (yes/no)  ")
                    while likedislike == "no":
                        password = ''.join([choice(list(printable)) for item in range(0, score)])
                        password2 = password.replace(" ", "")
                        print(password2)
                        likedislike = input("Вам понравился пароль?  (yes/no)  ")
                    else:
                        print("Спасибо за использование!")
                        break
