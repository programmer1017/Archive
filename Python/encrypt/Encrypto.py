import os
import time
import random

A = [113,127,131,137,139,149,151,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,
     283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,419,421,431,433,439,443,449,457,461,
     463,467,479,487,491,499]

BB = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
C = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p","a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
D = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P","A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]

q = random.choice(A)
w = random.choice(A) 
e = random.choice(A)
r = random.choice(A)
t = random.choice(A)
y = random.choice(A)
u = random.choice(A)
i = random.choice(A)
o = random.choice(A)
p = random.choice(A)
a = random.choice(A)
s = random.choice(A)
d = random.choice(A)
f = random.choice(A)
g = random.choice(A)
h = random.choice(A)
j = random.choice(A)
k = random.choice(A)
l = random.choice(A)
z = random.choice(A)
x = random.choice(A)
c = random.choice(A)
v = random.choice(A)
b = random.choice(A)
n = random.choice(A)
m = random.choice(A)


B = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m]



def num():
    n = random.sample(A,26)

def yn():
        yn_value = str( input( "Restart Program Again? [Y/N]" ) )
        if yn_value == "Y":
            main()
        elif yn_value == "N":
            os.system("pause")
        else:
            print("Error... Type Y or N")
            yn()


print("Making Cryptograms...")
time.sleep(1)
abc = int(input("What do you prefer? Making Cryptograms(type 1) or Decoding Cryptograms(type 2)"))

def main():
    if abc == 1:
        print("Setting Secret Key...")
        time.sleep(1)
        sk = int(input("Set Secret Key by number...   "))
        sen = str(input("Write a Sentence that you want to make Cryptograms...   "))
        if sk == 0:
            print("Error... Secret Key can't be 0...")
            yn()
        cryptogram_sentence = ""
        for anything in B:
            num( anything )
        for qw in sen:
            if qw == " ":
                print("Error... Sentence can't have space...")
                yn()
            else:
                if qw == "q" or qw == "Q":
                    tt = sk*q
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "w" or qw == "W":
                    tt = sk*w
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "e" or qw == "E":
                    tt = sk*e
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "r" or qw == "R":
                    tt = sk*r
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "t" or qw == "T":
                    tt = sk*t
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "y" or qw == "Y":
                    tt = sk*y
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "u" or qw == "U":
                    tt = sk*u
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "i" or qw == "I":
                    tt = sk * i
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "o" or qw == "O":
                    tt = sk*o
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "p" or qw == "P":
                    tt = sk*p
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "a" or qw == "A":
                    tt = sk*a
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "s" or qw == "S":
                    tt = sk*s
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "d" or qw == "D":
                    tt = sk*d
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "f" or qw == "F":
                    tt = sk*f
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "g" or qw == "G":
                    tt = sk*g
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "h" or qw == "H":
                    tt = sk*h
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "j" or qw == "J":
                    tt = sk*j
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "k" or qw == "K":
                    tt = sk*k
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "l" or qw == "L":
                    tt = sk*l
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "z" or qw == "Z":
                    tt = sk*z
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "x" or qw == "X":
                    tt = sk*x
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "c" or qw == "C":
                    tt = sk*c
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "v" or qw == "V":
                    tt = sk*v
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "b" or qw == "B":
                    tt = sk*b
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "n" or qw == "N":
                    tt = sk*n
                    cryptogram_sentence = cryptogram_sentence + str(tt)
                if qw == "m" or qw == "M":
                    tt = sk*m
                    cryptogram_sentence = cryptogram_sentence + str(tt)
        print("Cryptogram Sentence is...")
        print( cryptogram_sentence + str(q) + str(w) + str(e) + str(r) + str(t) + str(y) + str(u) + str( i ) + str( o ) + str( p ) + str( a ) + str( s ) + str( d ) + str( f ) + str( g ) + str( h ) + str( j ) + str( k ) + str( l ) + str( z ) + str( x ) + str( c ) + str( v ) + str( b ) + str( n ) + str( m ) )
        yn()



main()
