def my_pow(x, y):
    num = 1
    for i in range(y):
        num *= x
    return num

print(my_pow(2, 4))
print(pow(3, 4))