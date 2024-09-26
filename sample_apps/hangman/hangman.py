# import random

# # words = ["apple", "banana", "orange", "grape"]

# hangman_draw = {0: ("   ",
#                     "   ",
#                     "   "),
#                 1: (" o ",
#                     "   ",
#                     "   "),
#                 2: (" o ",
#                     " | ",
#                     "   "),
#                 3: (" o ",
#                     "/| ",
#                     "   "),
#                 4: (" o ",
#                     "/|\\",
#                     "   "),
#                 5: (" o ",
#                     "/|\\",
#                     "/  "),
#                 6: (" o ",
#                     "/|\\",
#                     "/ \\"),}

# # for line in hangman_draw[6]:
# #     print(line)

# # 행맨 그리기 함수
# def display_man(wrong_answer):
#   for line in hangman_draw[wrong_answer]:
#     print(line)

# # 힌트 출력 함수 
# def display_hint(hint):
#   print(" ".join(hint))

# # 정답 출력 함수
# def display_answer(answer):
#   print(" ".join(answer))

# def main():
#   guessed_letters = set() # 초기화 set
#   is_run = True
#   answer = random.choice(words)
#   hint = ["_"] * len(answer)
#   wrong_answer = 0

#   # print(hint)

#   while is_run:
#     # print(guessed_letters)

#     guess = input("알파벳을 입력해주세요: ").lower()

#     if len(guess) != 1 or not guess.isalpha():
#       print("알파벳 한 글자만 입력해주세요.")
#       continue

#     if guess in guessed_letters:
#       print("이미 입력한 알파벳 입니다.")
#       continue

#     guessed_letters.add(guess)
#     # print(guessed_letters)

#     # print(answer)

#     # 입력한 글자가 정답에 포함되어 있는지 확인
#     if guess in answer:
#       for i in range(len(answer)):
#         if guess == answer[i]:
#           hint[i] = guess
#     else:
#       wrong_answer += 1
    
#     if "_" not in hint:
#       print("살았습니다.")
#       display_man(wrong_answer)
#       display_answer(answer)
#       is_run = False
#     elif wrong_answer >= len(hangman_draw) -1:
#       print("죽었습니다.")
#       display_man(wrong_answer)
#       display_answer(answer)
#       is_run = False

# if __name__ == "__main__": 
#     main()


from hangman_words import words
import random


# words = ["apple", "banana", "orange", "grape"]

hangman_draw = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),  # 패배 시 그림 완성
}

# 행맨 그리기 함수
def display_man(wrong_answer):
    for line in hangman_draw[wrong_answer]:
        print(line)

# 힌트 출력 함수 
def display_hint(hint):
    print(" ".join(hint))

# 정답 출력 함수
def display_answer(answer):
    print(f"정답은: {answer}")

def main():
    guessed_letters = set()  # 이미 입력한 알파벳 저장
    is_run = True
    answer = random.choice(words)  # 랜덤으로 단어 선택
    hint = ["_"] * len(answer)  # 정답 길이에 맞는 빈 힌트 초기화
    wrong_answer = 0  # 틀린 시도 횟수

    print("단어 힌트: ", end="")
    display_hint(hint)  # 첫 번째 힌트 출력

    while is_run:
        guess = input("알파벳을 입력해주세요: ").lower()

        # 입력 유효성 검사
        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 입력해주세요.")
            continue

        # 이미 입력한 알파벳인지 확인
        if guess in guessed_letters:
            print("이미 입력한 알파벳입니다.")
            continue

        guessed_letters.add(guess)  # 입력된 알파벳 추가

        # 입력한 글자가 정답에 포함되어 있는지 확인
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_answer += 1

        # 상태 출력: 힌트 및 행맨 그리기
        display_hint(hint)
        display_man(wrong_answer)

        # 게임 종료 조건
        if "_" not in hint:  # 모든 글자를 맞춘 경우
            print("축하합니다! 단어를 맞추셨습니다!")
            display_answer(answer)
            is_run = False
        elif wrong_answer >= len(hangman_draw) - 1:  # 틀린 횟수가 한계에 도달한 경우
            print("패배하셨습니다. 행맨이 완성되었습니다.")
            display_answer(answer)
            is_run = False

if __name__ == "__main__": 
    main()
