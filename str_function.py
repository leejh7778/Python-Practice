# center - 문자열을 중앙에 위치시킨다.
a = "world!"
b = a.center(20) # 20개의 자리를 만들고, 그 중앙에 위치
c = "abcdefghijklmnopqrst"
# print(b)
# print(c)

# count - 문자열에서 특정 문자열의 개수를 반환
d = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when"

e = d.count("Lorem")
f = d.count(" ")
# print(e)
# print(f)

# endswith - 문자열이 특정 문자열로 끝나는지 확인
print(d.endswith("when."))

# replace - 문자열에서 특정 문자열을 다른 문자열로 교체
print(d.replace("Lorem", "Hello"))

# split - 문자열을 특정 문자열 기준으로 나누고 리스트로 반환
g = d.split(" ") # 두번째 파라미터는 배열의 개수를 제한한다. 2개로 제한하면 2개까지만 나눈다.
print(g)
