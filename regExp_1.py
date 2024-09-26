# special sequences : \문자 사용
import re

a = "marshall lives in Korea, Incheon 13"
b = re.findall(r"\Amarshall", a) # 문자열의 시작이 marshall인 문자열

c = re.findall(r"marshall\B", a) # marshall 문자열이 뒤에 오지 않는 문자열
d = re.findall(r"\Bmarshall", a) # marshall 문자열이 앞에 오지 않는 문자열
e = re.findall(r"\bmarshall", a) # marshall 문자열이 단어의 시작에 오면 매칭

f = re.findall(r"\d", a) # 숫자가 있는 문자열
g = re.findall(r"\D", a) # 숫자가 아닌 문자열 : 공백, 특수문자 포함
h = re.findall(r"\s", a) # 공백 문자열
i = re.findall(r"\w", a) # 문자와 숫자
j = re.findall(r"13$", a) # 문자열 문장의 끝과 매칭


# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(h)
# print(i)
print(j)

