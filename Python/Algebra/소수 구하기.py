import os

x = int(input("1부터 무슨 숫자까지의 소수를 구할까요??  "))
d = 3
i = 2
f = 1

print("소수")
print("2")
while d <= x:
    if d > i:
        if d % i == 0:
           d = d + 1
           i = 2
        else:
            i = i + 1
    if d == i:
        print(d)
        f = f + 1
        d = d + 1
        i = 2

print("1부터 ", x,"까지 소수의 개수는 ", f,"개입니다.")
    
   
os.system('pause')
