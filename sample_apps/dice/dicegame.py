# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

import random

dice_block = {
  1: ("┌───────┐",
      "│       │",
      "│   ●   │",
      "│       │",
      "└───────┘"),
  2: ("┌───────┐",
      "│ ●     │",
      "│       │",
      "│     ● │",
      "└───────┘"),
  3: ("┌───────┐",
      "│ ●     │",
      "│   ●   │",
      "│     ● │",
      "└───────┘"),
  4: ("┌───────┐",
      "│ ●   ● │",
      "│       │",
      "│ ●   ● │",
      "└───────┘"),
  5: ("┌───────┐",
      "│ ●   ● │",
      "│   ●   │",
      "│ ●   ● │",
      "└───────┘"),
  6: ("┌───────┐",
      "│ ●   ● │",
      "│ ●   ● │",
      "│ ●   ● │",
      "└───────┘"),
}

dice = []
total = 0

num_of_dice = int(input('주사위를 몇 번 던지겠습니까? '))

for di in range(num_of_dice):
  dice.append(random.randint(1, 6))

print(dice)

for di in range(num_of_dice):
  for line in dice_block.get(dice[di]): #핵심
    print(line)

for di in dice:
  total += di

print(f"주사위의 합은 {total}입니다.")
