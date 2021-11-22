s = "banana, grape, apple"
x = s.split(',')
print(x)
print(x[1])
for i in x:
    print(i)

s2 = "a:b:c:d"
x2 = s2.split(':')
print(x2)
for i in x2:
    print(i)

n1, n2 = input("두 수 입력 : ").split()
add = int(n1) + int(n2)
print(add)
