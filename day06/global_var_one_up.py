#전역변수 - global 키워드
#x = 5 << 전역변수

def one_up():
    global x  #지역변수
    x += 1
    return x


x = 5
print(one_up())
print(one_up())