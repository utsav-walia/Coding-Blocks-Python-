from math import sqrt

A = int(input())
a = int()
b = int()

if A>0 and a<=b and (a,b)>0 and A == a+b and sqrt(A) < (sqrt(a)+sqrt(b)):
    print((a,sqrt(A)) + (sqrt(a),sqrt(b)))

else:
    a = 0
    print((a,sqrt(A)))
