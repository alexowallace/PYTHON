s = {2,4,6,8}
h = {3,5,7,8,6}
e = set()#empty sets

print(s , type(s))

s.add(455)
print(s , type(s))
s.remove(4)
print(s , type(s))
print(len(s))

print(s.union(h))
print(s.intersection(h))
print(s-h)
print({2,4}.issubset(s))
print(s.issuperset({4,6}))


num = set()
n = input("enter num 1: ")
num.add(int(n))
n = input("enter num 1: ")
num.add(int(n))
n = input("enter num 1: ")
num.add(int(n))
n = input("enter num 1: ")
num.add(int(n))
n = input("enter num 1: ")
num.add(int(n))
n = input("enter num 1: ")
num.add(int(n))
n = input("enter num 1: ")
num.add(int(n))
print(num)

s1 = set()
s1.add(18)
s1.add("18")
print(s1)

























