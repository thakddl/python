import random

lottoNums = []
ranNum = random.random()

while len(lottoNums) < 6:
    ranNum = random.random()
    lottoNum = int(ranNum*45+1)
    check = True
    for item in lottoNums:
        if item == lottoNum:
            check == False
    if check:
        lottoNums.append(lottoNum)

print(lottoNums)
# lottoNums2 = []
#
# while len(lottoNums2) < 6:
#     ranNum = random.random()
#     lottoNum = int(ranNum*45+1)
#     if lottoNum not in lottoNums2:
#         lottoNums2.append(lottoNum)
#
# print(lottoNums2)