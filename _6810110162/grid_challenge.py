def grid_challenge(grid: list[str]) -> str:
    
    sorted_grid = [sorted(row) for row in grid]
    num_cols = len(sorted_grid[0])
    for col in range(num_cols):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    return "YES"