startNumInput = input("첫수를 적으세요:")
endNumInput = input("끝수를 적으세요:")

startNum = int(startNumInput)
endNum = int(endNumInput)

arr = range(startNum, endNum+1)
mySum = 0
for i in arr:
    mySum += i

# print(f"{startNum}에서 {endNum}까지의 합은 {mySum}입니다.")
print("{}에서 {}까지의 합은 {}입니다.".format(startNum, endNum, mySum))

