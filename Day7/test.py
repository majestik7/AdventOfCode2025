def unique_paths(m, n):
    """
    Calculates the number of unique paths from the top-left corner
    to the bottom-right corner of an m x n grid,
    assuming movement is restricted to down or right.

    Args:
        m: The number of rows in the grid.
        n: The number of columns in the grid.

    Returns:
        The total number of unique paths.
    """
    # Create a 2D array (dp table) to store the number of paths to each cell
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Initialize the first row and first column
    # There's only one way to reach any cell in the first row (by moving right)
    for j in range(n):
        dp[0][j] = 1
    # There's only one way to reach any cell in the first column (by moving down)
    for i in range(m):
        dp[i][0] = 1

    # Fill the dp table
    # For any other cell (i, j), the number of paths to reach it
    # is the sum of paths from the cell above (i-1, j) and the cell to its left (i, j-1)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # The result is the number of paths to the bottom-right corner
    return dp[m-1][n-1]

# Example usage:
rows = 3
cols = 7
total_paths = unique_paths(rows, cols)
print(f"Number of unique paths in a {rows}x{cols} grid: {total_paths}")