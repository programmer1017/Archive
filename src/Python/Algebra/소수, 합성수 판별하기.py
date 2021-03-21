import os


n = int(input("소수인지 판별하려는 수는??  "))
i = 2
if n == 1:
    print("1은 소수도 합성수도 아닌 단위수입니다.")
else:
    while n >= i:
        if n > i:
            if n % i == 0:
                print(n, "은(는) 소수가 아닌 합성수입니다.")
                break
            else:
                i = i + 1
        if n == i:
            print(n, "은(는) 소수입니다.")
            break

os.system('pause')
