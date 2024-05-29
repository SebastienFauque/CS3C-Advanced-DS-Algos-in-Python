def add_nums(upper, current_sum = 0):
    if upper <= 0:
        return current_sum

    current_sum += upper

    return add_nums(upper - 1, current_sum)

print("TEST CASES")

nums = [1,2,3,4,5]

# for num in nums:
#     print(add_nums(num, 0))

def fibonacci(n):