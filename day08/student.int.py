from classlib.student import Student

# s = Student("김하나", 3)
# print(s)

s = [
    Student("김하나", 3),
    Student("이두울", 1),
    Student("박세엣", 2)
]

print("******* 학생 명단 *******")
for i in s:
    print(i)