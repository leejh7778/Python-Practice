# while : 조건이 참인 동안 반복된다. 멈추는 조건을 설정하지 않으면 무한루프가 된다.

i = 1

# while i < 10:

#   i += 1  
#   if i == 5:
#     continue

#   print(i)

while i < 5:
  print(i)
  i += 1
  if i == 3:
    break

  else:
    print("i is no longer less than 5")
  