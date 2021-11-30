class Student:
    def __init__(self):
        self.name = "콩쥐"
        self.grade = 1
        print("생성자 함수입니다.")
    def learn(self):
        return "수업을 듣습니다."

s = Student()
print("이름 : " + s.name)
print("학년 : " + str(s.grade))
print(s.learn())