"""
this program is made by Junhyuck Lee(@programmer1017) and Jaeseong Hyun(@JaeseongHyun0906)

2020, All Rights Reserved, under MIT License.

Thanks to Jaeseong Hyun, helped making this program a lot.
"""
import os

n = ""

x = int(input("Enter the number to factorize: "))

if x == 1:
    print("1 is neither prime number nor composition number.")

d = 2
print("factorizing ", x, "...")
while d <= x:
    if x % d == 0:
        if n == "":
            n = n + str(d)
        else:
            n = n + "*" + str(d)
        x = x / d
    else:
        d = d + 1

print(n)
os.system('pause')



