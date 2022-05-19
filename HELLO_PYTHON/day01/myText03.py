startNumInput = input("첫수를 적으세요:")
endNumInput = input("끝수를 적으세요:")
drainNumInput = input("배수를 적으세요:")

startNum = int(startNumInput)
endNum = int(endNumInput)

drainNum = int(drainNumInput)

arr = range(startNum, endNum+1)
mySum = 0
for item in arr:
    if item % drainNum == 0:
        mySum += item

print("{}부터 {}까지 {}배수의 합은 {}입니다.".format(startNum, endNum, drainNum, mySum))