#재기 함수
def facto(n):
    if n <= 1:      #최종값 마지막값
        return 1
    else:
        return n * facto(n-1)  #마지막보다 큰값

print(facto(1))
print(facto(2))
print(facto(3))