import  math
num = int(input())
primeNum = True
sqrRt = math.floor(math.sqrt(num))
counter = 0
for i in range(2,sqrRt+1):
    if num % i == 0:
        counter += 1
if counter > 0:
    primeNum = False
print(primeNum)