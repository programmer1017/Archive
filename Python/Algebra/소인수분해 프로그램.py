import os

x = int(input("Enter the number> ")) #change the input because of UnicodeError
d = 2


final_prime_list = []
final_number_list = []
while d <= x:
     n = 0 #이건 리스트에 요소를 1번만 추가하기 위한 변수임.
     if x % d == 0:
         final_prime_list.append(d)
         while n == 0:
              final_number_list.append(d)
              n = n+1
          

         x = x / d
     else:
          d = d + 1

print(final_prime_list)
print(final_number_list)

def main():
     pass




os.system('pause')


"""
변수 d를 찾았다고 하면, 리스트에 추가합니다. 나중에 리스트에 있는 d의 개수를 보고 다른 변수에 저장하여 출력합니다.
"""