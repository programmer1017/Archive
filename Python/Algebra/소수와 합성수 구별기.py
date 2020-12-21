import sys
"""
Copyright 2019 이준혁. All rights reserved.
"""

"""
<program introduction>
이 프로그램은 소수인지 합성수인지를 구별하는 프로그램입니다. 
나눠지는 수를 일일이 데이터베이스에 저장해야 해서 개선이 필요할 듯 보입니다. 
2019/12/21(토)
+12/21
line 35 else 구문을 처리를 다르게 해서 보완되었습니다.
"""

num = input("소수인지 아닌지 알려면 수를 입력하세요> ")
num = int(num)


def play():
    if num < 0:
        print("마이너스 값은 소수도 합성수도 아닙니다")
        sys.exit()
    if num % 2 == 0:
        print("합성수입니다")
    elif num % 3 == 0:
        print("합성수입니다")
    elif num % 5 == 0:
        print("합성수입니다")
    elif num % 7 == 0:
        print("합성수입니다")
    elif num % 11 == 0:
        print("합성수입니다")
    elif num % 13 == 0:
        print(" 합성수입니다")
    else:
        print("소수입니다")


def prevent():
    if num == 1:
        print("1은 소수도 합성수도 아닙니다")
        sys.exit()
    if num == 0:
        print("0으로 소수도 합성수도 아닙니다")
        sys.exit()
    if num == 2:
        print("소수입니다")
    elif num == 3:
        print("입니다")
    elif num == 5:
        print("소수입니다")
    elif num == 7:
        print("소수입니다")
    elif num == 11:
        print("소수입니다")
    elif num == 13:
        print("소수입니다")
    elif num == 17:
        print("소수입니다")
    elif num == 19:
        print("소수입니다")
    elif num == 23:
        print("소수입니다")
    else:
        play()


prevent()
