a = ["강아지", "고양이", "고양이", "햄스터", "토끼", "고슴도치", "앵무새", "korea"]
b = ["3", "5", "1", "7", "9"]

# for i in a:
#   print(i)

# 1. sort : 정렬
a.sort()
b.sort()
# print(a)
# print(b)
b.sort(reverse=True) # 역순정렬
# print(b)

# 2. copy: 리스트 복사
# c = a.copy()
# print(a)
# print(c)
# a[0] = "도마뱀"
# print(a)
# print(c)

# 3. list() : 리스트를 담아서 새로운 리스트를 반환

# c = list(a)
# print(c)

# c[0] = "도마뱀"

# print(a)
# print(c)

# # 4. extend(): 리스트를 합친다
# a.extend(b)
# print(a)

# 단순 합치기
# k = a + b
# print(k)

# 반복문으로 합치기
for x in b:
  a.append(x)
print(a)

# 5. count(): 리스트 안에 특정 값이 몇 개 있는지 확인
print(a.count("강아지"))
print(len(a)) # 리스트 요소의 개수