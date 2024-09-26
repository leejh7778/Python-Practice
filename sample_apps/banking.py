# 잔액 보기 : 함수
# 1번 입력 시 : 잔액을 출력한다.

# 입금함수 : 함수
# 2번 입력 시 : 입금할 금액 입력을 받는다.
# 입금할 금액이 0보다 작거나 문자일 경우 예외처리를 한다.

# 출금함수 : 함수
# 3번 입력 시 : 출금할 금액 입력을 받는다.
# 출금할 금액이 0보다 작거나 문자일 경우 예외처리를 한다.
# 출금할 금액이 잔액보다 클 경우 예외처리를 한다.

# 종료 : 함수
# 4번 입력 시 : 프로그램을 종료한다.

# 잔액보기
# def show_balance(balance):
#    print(f"현재 잔액은 {balance}원 입니다.")
  
# # 입금하기
# def deposit():
#    while True:
#       amount = input("입금할 금액을 입력해 주세요: ")

#       try:
#          amount = int(amount)
#       except ValueError:
#          print("숫자를 입력해 주세요.")
#          continue
         
#       if amount <= 0:
#          print("0보다 큰 숫자를 입력해 주세요.")
#          return 0
#       else:
#          return amount

# # 출금하기
# def withdraw(balance):
#    while True:
#       amount = input("출금할 금액을 입력해 주세요: ")

#       try:
#          amount = int(amount)
#       except ValueError:
#          print("숫자를 입력해 주세요.")
#          continue
      
#       if amount > balance:
#          print("잔액이 부족합니다.")
#          return 0
#       elif amount <= 0:
#          print("0보다 큰 숫자를 입력해 주세요.")
#          return 0
#       else:
#          return amount


# # 메인 로직이 들어가는 함수
# def main():
#   # 숫자 선택 로직
#   # 숫자 선택 조건에 다른 함수 호출
#   # 프로그램 종료 출력(print)
#   balance = 0
#   is_run = True

#   while is_run:
#      print("1. 잔액보기")
#      print("2. 입금하기")
#      print("3. 출금하기")
#      print("4. 종료")

#      choice = input("1~4번 중 선택해 주세요: ")

#      if choice == "1":
#         show_balance(balance)
#      elif choice == "2":
#         balance += deposit()
#      elif choice == "3":
#         balance -= withdraw(balance)
#      elif choice == "4":
#         is_run = False
#      else:
#         print("1~4번 중 선택해 주세요.")
#         continue
#   print("프로그램 종료")


# 잔액 보기 함수
balance = 0

def check_balance(balance):
    print(f"현재 잔액: {balance}원")

# 입금 함수
def deposit(balance):
    try:
        amount = int(input("입금할 금액을 입력하세요: "))
        if amount <= 0:
            print("입금 금액은 0보다 커야 합니다.")
        else:
            balance += amount
            print(f"{amount}원이 입금되었습니다. 현재 잔액: {balance}원")
    except ValueError:
        print("유효한 금액을 입력하세요. (숫자만 입력 가능합니다)")
    return balance  # 새로운 잔액 반환

# 출금 함수
def withdraw(balance):
    try:
        amount = int(input("출금할 금액을 입력하세요: "))
        if amount <= 0:
            print("출금 금액은 0보다 커야 합니다.")
        elif amount > balance:
            print(f"출금 금액이 잔액({balance}원)보다 큽니다. 출금할 수 없습니다.")
        else:
            balance -= amount
            print(f"{amount}원이 출금되었습니다. 현재 잔액: {balance}원")
    except ValueError:
        print("유효한 금액을 입력하세요. (숫자만 입력 가능합니다)")
    return balance  # 새로운 잔액 반환

# 종료 함수
def exit_program():
    print("프로그램을 종료합니다.")
    exit()

# 메인 로직이 들어가는 함수
def main():
    balance = 0  # 초기 잔액
    while True:
        print("\n1: 잔액 보기")
        print("2: 입금하기")
        print("3: 출금하기")
        print("4: 종료하기")
        
        try:
            choice = int(input("원하는 작업의 번호를 선택하세요: "))
            
            if choice == 1:
                check_balance(balance)
            elif choice == 2:
                balance = deposit(balance)  # 함수 반환값으로 잔액을 업데이트
            elif choice == 3:
                balance = withdraw(balance)  # 함수 반환값으로 잔액을 업데이트
            elif choice == 4:
                exit_program()
            else:
                print("잘못된 입력입니다. 1~4 사이의 숫자를 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

# 프로그램 시작
if __name__ == "__main__": 
    main()
