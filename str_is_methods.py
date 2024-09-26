# 어떠한 문자열 또는 숫자 등이 특정한 형식을 가지고 있는지를 확인하는 메서드들

# 1. isalpha(): 문자열이 모두 알파벳인지 확인
a = "abc"
b = "Abc"
c = "a b c"
d = "abc123"

# print(a.isalpha()) # True
# print(b.isalpha()) # True
# print(c.isalpha()) # False (공백이 있기 때문)
# print(d.isalpha()) # False (숫자가 있기 때문)

# 2. isnumeric(): 문자열이 모두 숫자인지 확인 - 확인 문자는 문자 형태의 숫자여야 한다.
e = 123
f = "123"

# print(e.isnumeric()) # 오류 발생
# print(f.isnumeric())

# 4. isalnum(): 문자열이 숫자 또는 알파벳인지 확인
g = "123"
h = "abc"
i = "123abc"
j = "123 abc"

# print(g.isalnum())
# print(h.isalnum())
# print(i.isalnum())
# print(j.isalnum())

# 4. isspace(): 문자열이 모두 공백인지 확인
k = " "
l = ""

# print(k.isspace())
# print(l.isspace())

# 5. join(): 문자열을 연결하여 새로운 문자열 반환
my_list = ["aa-bb-cc", "dd-ee-ff", "gg-hh-ii"]
rs = "/".join(my_list)

my_tup = ("aa", "bb", "cc")
rs_tup = " ".join(my_tup)

print(rs)
print(rs_tup)

# 6. startwith(): 문자열이 특정한 문자로 시작하는지 확인
a1 = "Hello, my name is joonghoon"
a2 = a1.startswith("Hello")
print(a2)

# 7. endswith(): 문자열이 특정한 문자로 끝나는지 확인
a3 = "Hello, my name is joonghoon"
a4 = a3.endswith("joonghoon")
print(a4)

# 8. splitlines(): 문자열을 라인 단위로 분리하여 새로운 리스트 반환
a5 = "Hello, \nmy name is joonghoon"
print(a5.splitlines())

# 9. isdisit(): 문자열이 모두 숫자인지 확인
a6 = "123"
a7 = 123
a8 = "abc"
print(a6.isdigit())
# print(a7.isdigit()) 에러
print(a8.isdigit())
