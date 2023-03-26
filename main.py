from random import choice
from string import printable


status = False
score = int(input("Задайте длинну пароля в диапазоне от 7 до 20 (число): "))
while score > 20 or score < 7:
    if score > 20:
        print("Пароль слишком длинный")
    elif int(score) < 7:
        print("Пароль слишком короткий")
    score = int(input("Какова длинна пароля?"))
else:
    while status == False :
        password = ''.join([choice(list(printable)) for item in range(0, score)])
        password2 = password.replace(" ", choice(list(printable)))
        print(password2)
        likedislike = input("Вам понравился пароль?  (да/нет): ")
        if likedislike == "да":
            status = True
