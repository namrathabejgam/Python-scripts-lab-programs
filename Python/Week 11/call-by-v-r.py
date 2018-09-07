def func2(list):
  print(list)
  list += [47,11]
  print("Inside function:",end=' ')
  print(list)
print("Call by Reference")
fib = [0,1,1,2,3,5,8]
func2(fib)
print("Outside function:",end=' ')
print(fib)
print("Call by value")
fib = [0,1,1,2,3,5,8]
func2(fib[:])
print("Outside function:",end=' ')
print(fib)
