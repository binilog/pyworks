#지역변수와 전역변수
x = 5

def one_up():
    x = 1   #지역변수
    x += 1
    return x

print(one_up())
print(one_up())
print(x)