# 문자열은 자체적으로 리스트 형태로 사용할 수 있다.
# 따라서 인덱싱이 가능하고, 인덱싱은 제로 베이스 인덱싱이다.
# 이러한 특징을 사용하여 문자열을 컨트롤 할 수 있다.

a = 'LoremIpsumissimplydummytext'
# print(a[0])
# print(a[1])
# print(a[2])

# print(a[-1])
# print(a[-2])

# a = 'LoremIpsumissimplydummytext'
# print(a[0:5]) # 0보다 크고 5보다 작은 인덱스 출력
# print(a[1:5])

# print(a[:5]) # 처음부터 5번보다 작은 인덱스 출력
# print(a[5:]) # 5번 인덱스부터 끝까지 출력
# print(a[:]) # 처음부터 끝까지 출력

b = a[:5]
c = a[5:10]
d = a[10:12]
e = a[12:18]
f = a[18:23]
g = a[23:]

print(b + ' ' + c + ' ' + d +' ' + e + ' ' + f + ' ' + g)

# str[start:end:step]
print(a[::2]) # 처음부터 끝까지 2칸씩 건너뛰어 출력
print(a[::-1]) # 처음부터 끝까지 역순으로 출력

# 대소문자 변환
h = " Joonghoon Lee "
print(h)
print(h.strip()) # 양쪽 공백을 제거
print(h.upper()) # 대문자
print(h.lower()) # 소문자

