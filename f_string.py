# f-string 포맷팅

# 1. + 연산자를 사용
name = "중훈"
friend = "박지성"
age = 20
print("제 이름은 " + name + "이고, 나이는 " + str(age) + "살 입니다")

# # 2. % 키워드 사용
# print("%s은 %s의 친구 입니다."%(name, friend))

# # 3. format 함수 사용
# print ("{}은 {}의 친구 입니다.".format(name, friend))

# # 4. f-string 사용
# # r을 사용하면 raw string으로 인식하여 이스케이프 문자를 문자로 처리한다.
# print(fr"{name}은 \n{friend}의 친구 입니다.")


# 숫자의 경우 연산이 가능하다.
x = 10
y = 20
print(f"{x} + {y} = {x + y}")

# 변수 블록{} 내에서는 문자열의 컨트롤도 가능하다.
z = "abcdefghijklmn"
print(f"{z[:5]}")
print(f"{z.upper()}")

from datetime import date
print(f"오늘은 {date.today()}일 입니다.")