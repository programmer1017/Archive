import random
import time

# 단어 리스트
w = ["Google", "Python", "Microsoft", "Australopithecus", "Stephen Hawking", "Pycharm", "Post malone", "love",
     "HP", "debug", "BTS", "oxford reading tree", "YouTube", "Android"]
n = 1  # 문제 번호
print("[타자 게임] 준비되면 Enter!")
input()  # 사용자가 엔터를 누를 때까지 기다림
start = time.time()  # 시작 시간을 기록

q = random.choice(w)  # 단어 리스트에서 요소를 랜덤하게 뽑는다.
while n <= 14:  # 문제를 열네 번 반복
    print("*문제", n)
    print(q)  # 문제를 출력
    x = input()  # 사용자 입력을 받는다.
    if q == x:  # 사용자가 올바르게 입력했는지?
        print("통과!")
        n = n + 1  # 문제 번호를 1 증가
        q = random.choice(w)  # 새 문제를 뽑는다.
    else:
        print("오타! 다시 도전!")

end = time.time()  # 종료 시간을 기록
et = end - start  # 실제로 걸린 시간을 계산
et = format(et, ".2f")  # 소수점 둘째 자리까지만 표시되도록 포맷팅
print("타자 시간 :", et, "초")

# this program is not belong to me.
# Source: Internet
