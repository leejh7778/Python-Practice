# List, Tuple, Set, Dictionary

# 1. List 중복 데이터 입력이 가능
a = ['사과', '배', '딸기', '포도', '수박']

# # 제로 베이스 인덱싱
# print(a[0])

# 자료 변경
a[0] = '키위'
# print(a)
# k = a[1:4] = ["복숭아", "체리"]
# print(a)


# 범위 지정
# print(a[1:3])
# print(a[0:3])
# print(a[:])
# print(a[-1])
# print(a[::2])

# append() : 리스트의 끝에 데이터 추가
a.append('망고')
print(a)

# insert(): 리스트의 특정 위치에 데이터 추가
a.insert(3, '오렌지')
print(a)

# remove(): 리스트의 파라미터로 지정된 데이터 삭제
a. remove('키위')
print(a)

# pop() : 리스트의 마지막 데이터 삭제 - 파라미터로 지정된 인덱스 삭제
a. pop()
print(a)
m = a. pop(3) # 삭제된 데이터를 변수에 저장
print(m)
print(a)

# del : 리스트의 인덱스를 지정하여 삭제 - 변수 저장 안됨
del a[0]
print(a)

# clear() : 리스트 전체를 지움 = 객체는 남아있음
a.clear()
print(a)