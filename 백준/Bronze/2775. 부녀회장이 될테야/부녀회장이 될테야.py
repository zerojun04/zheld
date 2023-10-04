import math

def res(a, b):
    c = math.factorial(a) / math.factorial(a - b) / math.factorial(b)
    return c
test = int(input())
k = [] #층수
n = [] #호수
for i in range(test):
    a = int(input())
    k.append(a)
    a = int(input())
    n.append(a)
for i in range(test):
    cmd = k[i]; gh = n[i]
    print(int(res(cmd + gh, gh - 1)))