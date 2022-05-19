import random
user = ""
com = ""
result = ""

arr = ["가위", "바위", "보"]
rnd = int(random.random()*3)

user = input("가위/바위/보를 선택하세요: ")
com = arr[rnd]


if user == com:
    result = "비김"
elif (user=="가위" and com=="보") or (user=="바위" and com=="가위") or (user=="보" and com=="바위"):
    result = "이김"
else:
    result = "짐"
    
print("나: {} \n컴퓨터: {} \n결과: {}".format(user, com, result))