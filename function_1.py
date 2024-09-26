# function: def 키워드를 사용

def my_func(name, age):
  print("age is {1}, name is {0}".format(name, age))

my_func("joonghoon", 20) # 호이스팅 되지 않음

# arbitary arguments: *args
def arb_func(*args):
  # print("age is {2}, name is {1}, address is {0}".format(args[0], args[1], args[2]))
  print(f"age is {args[2]}, name is {args[1]}, address is {args[0]}")

arb_func("inchenon", "joonghoon", 21)

# keyword arguments: **kwargs - dictionary 형태로 여러개의 변수를 받을 수 있음
def key_func(**kwargs):
  # print("age is {0}, name is {1}, address is {2}".format(kwargs['age'], kwargs['name'], kwargs['address']))

  print(f"age is {kwargs["age"]}, name is {kwargs["name"]}, address is {kwargs["address"]}")


key_func(age = 21, name = "joonghoon", address = "busan")