def merge_text(*text):
    sum_s = ""
    for s in text:
        sum_s += s
    return sum_s

str1 = merge_text("봄", "여름")
str2 = merge_text("봄","여름", "가을", "겨울")

print(str1)
print(str2)