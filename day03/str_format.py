# 문자열{}.format(a)

print("나는 사과를 {}개 먹었다.".format(100))

print("난 {}이다.".format("돼지"))

print("내 나이는 {}살이다. ".format(21))

print("나는 {}년도에 태어났다.".format(2001))

print("강사쌤은 {}를 가르치신다.".format("파이썬"))

print("나는 {}이 가고싶다.".format("집"))

print("또 응용버전을 하신다 정말 {}".format("피곤하다"))

year = 2001
age = 21
print("나는 {0}년생이고, 나이는 {1}살이다.".format(year, age))

public = "현대"
name = "소나타"
years = 2015
color = "검정"
cate = "중형세단"
print("나는 {0}사에서 만든 {4}차량 {2}연식인 {3}색 {1}를 탄다.".format(public, name, years, color, cate))

s = "Hello, welcome to my website!"
print(s.find('H'))
print(s.find('ll'))
print(s.find('k'))
s = s.find("welcome")
print(s)

str1 = " hi, soo!"
print(str1.strip())
print(str1.lstrip())

txt = " banana  "
x = txt.strip()
print("of all fruits", x, "is my favorite")