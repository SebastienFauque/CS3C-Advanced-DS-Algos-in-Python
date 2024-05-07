# Attempt 1
# def pascals_triangle(n: int, row_num = 0, old_row: list[int] = []) -> list:
#     """Implementation of Pascal's Triangle using recursion."""
#     if n <= 0:
#         """Edge case."""
#         return None
#     if row_num == n:
#         """Base case."""
#         return None
#
#
#     new_row = []
#     new_row.append(1)
#     if row_num > 1:
#
#     print(f"row {row_num}", new_row)
#     return pascals_triangle(n, row_num + 1, new_row)

# Attempt 2
def pascals_triangle(n: int, current_triangle: list = []):
    if len(current_triangle) == n:
        for row in current_triangle:
            print(row)
        return None

    # implement rules for adding a layer
    if len(current_triangle):
        max_row: list[int] = current_triangle[-1]
        new_row: list[int] = [1]
        for idx, item in enumerate(max_row):

            try:
                right: int = max_row[idx + 1]
                left: int = max_row[idx]
                new_row.append(left + right)
            except IndexError:
                new_row.append(1)
                current_triangle.append(new_row)
                return pascals_triangle(n, current_triangle)

            #print(new_row)

            # if right == 1:
            #     # end the row and append to current triangle
            #     current_triangle.append(new_row)
            #     return pascals_triangle(n, current_triangle)
    return pascals_triangle(n, [[1]])

print("TEST CASES ----------------------")
for n in range(1, 7):
    print(f"Case {n}: ")
    pascals_triangle(n)



