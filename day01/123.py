# 변수 사용하기 - 주석은 #을 사용
#- 한줄 주석 #을 사용
# 여러줄 주석을 """나 '''로 사용
print('******☆회원가입☆******')
userid = 'skt6124'
userpw = 'tmdql*****'
name = '승빈'
age = 21
phone = '010-6260-2951'
fun = '졸린다'

"""
print("  아이디 : ",     userid) 
print("비밀 번호: ",     userpw) 
print("  이 름  : ",       name) 
print("전화 번호: ",      phone) 
print("   나이  : ",        age) 
print("   상태  : ",        fun) 
"""
print("="*24)
print("  아이디 : "+     userid) 
print("비밀 번호: "+     userpw) 
print("  이 름  : "+       name) 
print("전화 번호: "+      phone)  
print("   상태  : "+        fun)
print("   나이  : "+   str(age))
