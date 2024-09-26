import random # 랜덤 모듈 임포트

top_number = input("숫자를 입력해 주세요: ") # 사용자로부터 숫자 입력 받기

if top_number.isdigit():
  top_number = int(top_number) # 입력 받은 숫자를 정수로 변환

  if top_number <= 0:
    print("1 이상의 숫자를 입력해 주세요.")
    quit()
else:
  print("숫자를 입력해 주세요")
  quit()

random_number = random.randint(1, top_number) # 1부터 입력값 사이의 난수 생성
guess_numer = 0 # 사용자가 추측한 숫자

print(random_number) # 무한 루프: 첫째 주의점은 자동으로 실행되는 코드에는 반드시 종료 조건이 있어야 한다. 두번째 주의점은 사용자가 종료 조건을 만족시킬 수 있는 코드를 작성해야 한다.
while True:
  guess_numer += 1 # 추측 횟수 증가
  user_guess = input("숫자를 입력해 주세요: ")

  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("숫자를 입력해 주세요.")
    continue #루프 시작으로 돌아가기

  if user_guess == random_number:
    print("정답 입니다.")
    break # 루프 종료
  elif user_guess > random_number:
    print("숫자가 큽니다.")
  else:
    print("숫자가 작습니다.")

print(f"정답을 맞추기 위해 {guess_numer}번 입력 했습니다.")