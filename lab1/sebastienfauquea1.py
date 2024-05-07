"""Tests to check the implementation of the node and stack classes."""
from sebastienfauquestack import Stack

def is_matching_pair(opening, closing):
    pairs = {'(': ')', '{': '}', '[': ']'}
    return pairs.get(opening) == closing


def is_balanced(expression):
    stack = Stack.create_stack()
    for i, char in enumerate(expression):
        if char in '({[':
            stack.push((char, i))  # Push both the symbol and its index
        elif char in ')}]':
            if stack.is_empty():
                print(f"Unmatched closing symbol '{char}' at index {i}")
                return False
            popped_symbol, popped_index = stack.pop()
            if not is_matching_pair(popped_symbol, char):
                print(f"Unmatched closing symbol '{char}' at index {i}")
                return False

    if not stack.is_empty():
        popped_symbol, popped_index = stack.pop()
        print(f"Unmatched opening symbol '{popped_symbol}' at index {popped_index}")
        return False
    return True


# Test cases 1
test_cases = [
    "([|)]", # Not balanced
    "() (() [()])", # Balanced
    "{{([][])}()}", # Balanced
]

for i, test_case in enumerate(test_cases):
    if is_balanced(test_case):
        print(f"Output {i}: Balanced")
    else:
        print(f"Output {i}: Not Balanced")

# Additional demonstrations, test cases 2
expressions = [
"(a + b) * [c - d]", # Balanced
"The quick [red] {fox} jumps over the lazy (dog}." # Not balanced.
]

print("Demonstration of non symbol characters:")
for i, test_case in enumerate(expressions):
    print(f"Expression {i}: {test_case}")
    if is_balanced(test_case):
        print(f"Output {i}: Balanced")
    else:
        print(f"Output {i}: Not Balanced")

"""
Time complexity: O(n)
Space complexity: O(n)

/Users/seb/git/cs3c-advanced-data-struc-algos-python/pythonProject/.venv/bin/python /Users/seb/git/cs3c-advanced-data-struc-algos-python/pythonProject/sebastienfauquea1.py 
Unmatched closing symbol ')' at index 3
Output 0: Not Balanced
Output 1: Balanced
Output 2: Balanced
Demonstration of non symbol characters:
Expression 0: (a + b) * [c - d]
Output 0: Balanced
Expression 1: The quick [red] {fox} jumps over the lazy (dog}.
Unmatched closing symbol '}' at index 46
Output 1: Not Balanced

Process finished with exit code 0
"""