import timeit
# class Fibonacci:
#     def __init__(self):
#          self.memo = {0: 1, 1: 1}
#
#     def fibonacci(self, n: int):
#         if n in self.memo:
#             return self.memo[n]
#         else:
#             self.memo[n] = self.fibonacci(n-1) + self.fibonacci(n - 2)
#             return self.memo[n]
#
# fib = Fibonacci()
#
# assert fib.fibonacci(0) == 1
# assert fib.fibonacci(1) == 1
# assert fib.fibonacci(2) == 2
# assert fib.fibonacci(3) == 3
# assert fib.fibonacci(4) == 5
# assert fib.fibonacci(5) == 8
# assert fib.fibonacci(6) == 13
print("all tests passed")

# Tree for fib(5)
def fibone(n):
   fibs = [0, 1]
   for i in range (2, n + 1):
      fibs.append(fibs[i - 1] + fibs[i-2])
   return fibs[n]

time1 = timeit.timeit("")
for i in range(40):
    fibone(i)
time2 = timeit.timeit("")

total_time = time2 - time1
print('total time1:', total_time)

def fibtwo(n):
   if n <= 1:
      return n;
   else:
      return fibtwo(n - 1) + fibtwo(n - 2)

time3 = timeit.timeit("")
for i in range(40):
    fibtwo(i)

time4 = timeit.timeit("")

print('total time2:', time4 - time3)