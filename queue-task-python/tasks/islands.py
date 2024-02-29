"""Template for programming assignment: number of islands."""
from typing import List
from collections import deque


def get_islands_count(grid: List[List[str]]) -> int:
    """Returns the number of islands in a given grid."""

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        """Perform BFS to explore all connected land cells."""
        queue = deque([(r, c)])
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # Explore in four directions
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands
