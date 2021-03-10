# 함수의 정의
def sumOfInteger(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

while True:
    n = input('input integer : ')
    if n != 'q':
        print(sumOfInteger(int(n)))
    else:
        break