# 문자열 조합 관련

a = "hello"
b = "world"

c = a + b
print(c)

# 문자열 포맷팅

name = "joonghoon"
age = 20

txt = "내 이름은 {}이고, 나이는 {}살 입니다.".format(name, age)

print(txt)

# f-string
f_txt = f"내 이름은 {name}이고, 나이는 {age}살 입니다."

# print(f_txt)

# 문자열 이스케이프
me = "Hello, My age is \\\"20\\\" years old." # \"20\"
print(me)

# 문자열 개행
me2 = "hello, \nmy name is joonghoon"
print(me2)

# 문자열 탭
me3 = "hello, \tmy name is joonghoon"
print(me3)

# 문자열 백스페이스
me4 = "hello, \b\b\bmy name is joonghoon"
print(me4)


