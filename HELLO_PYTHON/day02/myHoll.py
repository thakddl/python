import random

user = ""
com = ""
result = ""

user = input("홀/짝을 고르시오: ")
rnd = random.random()

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if com == user:
    result = "이김"
else:
    result = "짐"

print("나: {} \n컴퓨터: {} \n결과: {}".format(user, com, result))
