# 1. 입력 문자를 받는다. (c or f) - 대문자든 소문자든 상관없이 받는다
while True:
  unit = input("변환할 온도 체계를 입력해 주세요(c 또는 f): ").lower()

# 2. 입력 문자가 c 또는 f가 아니면 둘 중 하나만 입력하라고 출력한다.
  if unit == "c" or unit == "f":
    break
  else:
    print("c 또는 f만 입력해 주세요.")

# 3. 온도를 입력 받는다. (초기화 변수가 필요함)
c_or_f = ""
while True:
  temp = input("온도를 입력해 주세요: ")

# 4. 입력 받은 온도가 숫자가 아닌지 확인하고, 아니라면 숫자를 입력하라고 주문한다.

  try:
    temp = float(temp)
    break
  except ValueError:
    print(f"{temp}은(는) 문자입니다. 숫자로 입력해 주세요.")
  

# 5. 입력 받은 문자가 c 이면 화씨로 변환하고, f 이면 섭씨로 변환한다.
if unit == "c":
  c_or_f = "화씨"
  temp = (temp * 1.8) + 32
elif unit == "f":
  c_or_f = "섭씨"
  temp = (temp - 32) / 1.8

# 6. 변환된 온도를 출력한다.
print(f"입력하신 변환 온도는 {c_or_f}{temp:.2f}도 입니다.")

# 섭씨->화씨 [°F] = [°C] × 1.8 + 32
# 화씨->섭씨 [°C] = ([°F] − 32) / 1.8

# def convert_temperature():
#     while True:
#         scale = input("섭씨는 'C', 화씨는 'F'를 입력하세요: ").lower()
#         if scale != "c" and scale != "f":
#             print("C 또는 F만 입력해 주세요.")
#             continue
#         break

#     while True:
#         temp = input("온도를 입력하세요: ")
#         try:
#             temp = float(temp)  
#         except ValueError:
#             print(f"{temp}은(는) 숫자가 아닙니다. 숫자를 입력해 주세요.")
#             continue 
#         break

#     if scale == 'c':
#         converted_temp = temp * 1.8 + 32
#         print(f"섭씨 {temp}도는 화씨 {converted_temp:.2f}도입니다.")
#     else:
#         converted_temp = (temp - 32) / 1.8
#         print(f"화씨 {temp}도는 섭씨 {converted_temp:.2f}도입니다.")


# convert_temperature()

