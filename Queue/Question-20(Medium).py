# Question 200: Use a queue for BFS in a Snake and Ladder game.
from collections import deque

def min_dice_throws_snake_ladder(board_size, snakes, ladders):
    num_squares = board_size * board_size
    queue = deque([(1, 0)])
    visited = [False] * (num_squares + 1)
    visited[1] = True

    while queue:
        current_position, moves = queue.popleft()

        if current_position == num_squares:
            return moves

        for dice_roll in range(1, 7):
            next_position = current_position + dice_roll

            if 1 <= next_position <= num_squares:
                if next_position in ladders:
                    next_position = ladders[next_position]

                if next_position in snakes:
                    next_position = snakes[next_position]

                if not visited[next_position]:
                    visited[next_position] = True
                    queue.append((next_position, moves + 1))

    return -1

board_size = 10
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}
ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

min_moves = min_dice_throws_snake_ladder(board_size, snakes, ladders)

if min_moves != -1:
    print(f"Minimum dice throws to win: {min_moves}")
else:
    print("Cannot reach the end of the board.")