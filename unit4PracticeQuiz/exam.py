
def doubleDigits(num):
   if num < 0:
      return - doubleDigits(-num)
   elif num == 0:
      return 0
   else:
      digit = num % 10
      rest = num // 10
      return digit + 10 * digit + 100 * doubleDigits(rest)

print(doubleDigits(157))
print(doubleDigits(-321))