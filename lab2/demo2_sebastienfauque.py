import pytest
from sebastienfauqueLab2 import pascals_triangle

# print("TEST CASES ----------------------")
# for n in range(1, 7):
#     print(f"Case {n}: ")
#     pascals_triangle(n)



# Stack frame for stack frame up to 6.
# TEST CASES ----------------------
# Case 1:
# row 0  [1]
# Case 2:
# row 0  [1]
# row 1  [1, 1]
# Case 3:
# row 0  [1]
# row 1  [1, 1]
# row 2  [1, 2, 1]
# Case 4:
# row 0  [1]
# row 1  [1, 1]
# row 2  [1, 2, 1]
# row 3  [1, 3, 3, 1]
# Case 5:
# row 0  [1]
# row 1  [1, 1]
# row 2  [1, 2, 1]
# row 3  [1, 3, 3, 1]
# row 4  [1, 4, 6, 4, 1]
# Case 6:
# row 0  [1]
# row 1  [1, 1]
# row 2  [1, 2, 1]
# row 3  [1, 3, 3, 1]
# row 4  [1, 4, 6, 4, 1]
# row 5  [1, 5, 10, 10, 5, 1]

# myname = "sebastienfauque"
# mynamelength = len(myname)

# pascals_triangle(mynamelength)
# row 0  [1]
# row 1  [1, 1]
# row 2  [1, 2, 1]
# row 3  [1, 3, 3, 1]
# row 4  [1, 4, 6, 4, 1]
# row 5  [1, 5, 10, 10, 5, 1]
# row 6  [1, 6, 15, 20, 15, 6, 1]
# row 7  [1, 7, 21, 35, 35, 21, 7, 1]
# row 8  [1, 8, 28, 56, 70, 56, 28, 8, 1]
# row 9  [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# row 10  [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
# row 11  [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
# row 12  [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1]
# row 13  [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1]
# row 14  [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1]

#program output example for n = 3
# Stack frame for recursion depth 3.
# row 0  [1]
# row 1  [1, 1]
# row 2  [1, 2, 1]
