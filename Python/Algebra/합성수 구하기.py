import os

x = int(input("1부터 무슨 숫자까지의 합성수를 구할까요??  "))
d = 3
i = 2
f = 0

print("합성수")
while d <= x:
    if d > i:
        if d % i == 0:
            print(d)
            d = d + 1
            f = f + 1
            i = 2
        else:
            i = i + 1
    if d == i:
        d = d + 1
        i = 2

print("1부터 ", x,"까지 합성수의 개수는 ", f,"개입니다.")
    
   
os.system('pause')
