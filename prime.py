def is_prime(num):
  for element in range(2,num):
    if num % element == 0:
      print(num)
      print("NOT PRIME")
      return False
  print(num)
  print("PRIME")
  return True

x = int(input("enter:"))
is_prime(x)
