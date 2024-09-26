import re

# []: 문자 집합 검색

a = "marshall lives in Korea, Incheon 13"

b = re.findall("[img]", a) # i, m, g 중 하나라도 있으면 매칭
c = re.findall("[a-d]", a) # a부터 d까지 중 하나라도 있으면 매칭
d = re.findall("[^a-zA-z]", a) # 알파벳 문자가 아닌 문자열
e = re.findall("[0-9]", a) # 숫자가 있는 문자열
f = re.findall("[0-9][0-9]", a) # 두 자리 숫자가 있는 문자열

# search() : 객체 반환
g = re.search(r"\s", a) # 공백 문자 매칭
h = re.search(r"live", a) # live 문자열 매칭 

# split()

i = re.split(r"\s", a, 2) # 공백 문자열을 기준으로 나누기 : 3번째 파라미터는 나눈 횟수 지정,
#나누는 기준은 첫번째 매칭

# sub() : 대체

j = re.sub(r"\s", ":", a) # 공백을 클론으로 대체

print(j)
# print(g.start())
# print(g.end())