# employee.py 모듈 만들기
# Employee 클래스 생성

class Employee:
    serial_num = 1000 #기준값(클래스 변수)

    def __init__(self):
        Employee.serial_num += 1
        self._id = Employee.serial_num

    def getid(self):
        return self._id

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name


e1 = Employee()
e1.setname("김하늘")
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())

e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())
e1 = Employee()
print("사번 : ",e1.getid())




