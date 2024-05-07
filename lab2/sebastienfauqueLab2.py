def pascals_triangle(n: int, current_triangle: list = []):
    """Recursive implementation of Pascal's triangle.
    Params:
        n (int): Number of rows in the triangle.
        current_triangle (list of lists[int): current rows of the triangle
    """

    # Ending condition
    if len(current_triangle) == n:
        for idx, row in enumerate(current_triangle):
            print(f"row {idx} ", row)
        return None

    # implement rules for adding a layer
    if len(current_triangle):
        max_row: list[int] = current_triangle[-1]
        new_row: list[int] = [1]
        for idx in range(len(max_row)):

            try:
                right: int = max_row[idx + 1]
                left: int = max_row[idx]
                new_row.append(left + right)
            except IndexError:
                new_row.append(1)
                current_triangle.append(new_row)
                return pascals_triangle(n, current_triangle)

    # Solve the most simple case.
    return pascals_triangle(n, [[1]])





