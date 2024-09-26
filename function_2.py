# # defauly parameter values

# def default_func(country="Korea"):
#   print(f"I am from {country}")

# default_func()
# default_func("America")

# # collection parameter

# def collection_func(aaa):
#   for i in aaa:
#     print(i)

# # list
# collection_func(["korea", "america", "japan"])

# # tuple
# collection_func(("korea", "america", "japan"))

# # return value
# def return_func(a, b):
#   return a + b

# print(return_func(3, 4))

def prevnt_func(a, /):
  print(a)
  # pass

# prevnt_func(a=2) # error
# prevnt_func(1) # error
prevnt_func(3)


