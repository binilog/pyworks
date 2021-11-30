class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self): #객체의 멤버정보를 출력하는 함수
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)

if __name__ == "__main__": #name 변수의 이름이 main이라면
    s1 = Student("콩쥐", 1)
    print(s1)

    s2 = Student("팥쥐", 2)
    print(s2)