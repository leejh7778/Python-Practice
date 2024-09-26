# sleep 함수 : 일정 시간동안 프로그램을 멈추는 함수

import time

# time.sleep(3)

# print("3초가 지났습니다.")

# for x in reversed(range(0, 10, 2)):
#   print(x)

# 00: 01 : 10

# for : sleep(1)

# seconds = 70 % 60
# minutes = (70 // 60) % 60

# print(seconds)
# print(minutes)

my_time = input("초 단위 시간을 입력해 주세요: ")

try:
  my_time = int(my_time)
except ValueError:
  print("숫자만 입력해 주세요")
  exit()

# for x in reversed(range(0, my_time)):
for x in range(my_time, 0, -1):
  seconds = x % 60
  minutes = (x // 60) % 60
  # 02d : 2자리 숫자로 표현하되 1자리면 앞에 0이 붙는다
  print(f"{minutes:02d} : {seconds:02d}")
  time.sleep(1)







# def countdown(total_time):
#     for remaining_time in range(total_time, 0, -1):  
#         minutes = (remaining_time // 60) % 60 
#         seconds = remaining_time % 60
#         print(f"{minutes:02}:{seconds:02}")
#         time.sleep(1)                         
    
#     print("카운트다운 종료")


# start_time = int(input("시간을 초 단위로 입력하세요: "))
# countdown(start_time)


