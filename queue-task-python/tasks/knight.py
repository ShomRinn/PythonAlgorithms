"""Template for programming assignment: minimum knight moves."""
from typing import List
from collections import deque

def get_minimum_knight_moves(chessboard: List[List[str]]) -> int:
    """Returns the minimum number of knight moves to reach the destination point."""

    # Directions a knight can move
    directions = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

    # Find the starting position of the knight and the dimensions of the board
    for i in range(8):
        for j in range(8):
            if chessboard[i][j] == 'K':
                start = (i, j)
                break

    # Initialize the queue with the starting position and the initial move count
    queue = deque([(start, 0)])
    visited = set([start])

    # BFS
    while queue:
        (x, y), moves = queue.popleft()
        
        # Check if we've reached the destination
        if chessboard[x][y] == 'D':
            return moves

        # Explore all possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and chessboard[nx][ny] != 'O' and (nx, ny) not in visited:
                queue.append(((nx, ny), moves + 1))
                visited.add((nx, ny))

    return -1
