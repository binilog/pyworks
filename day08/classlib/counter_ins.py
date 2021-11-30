# Counter 클래스 만들기
class Counter:
    def __init__(self):
        self.x = 0
        self.x += 1

    def getcount(self):
        return self.x

c1 = Counter()
print(c1.getcount())

c2 = Counter()
print(c2.getcount())

c3 = Counter()
print(c3.getcount())

