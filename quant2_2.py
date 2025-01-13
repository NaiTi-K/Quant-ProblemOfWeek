import numpy as np

def coor_to_state(pos):
    return (pos[0] - 1) * 8 + pos[1] - 1


def precompute_knight_moves():
    moves = [(3, 1), (1, 3), (-1, 3), (-3, 1),
             (-3, -1), (-1, -3), (1, -3), (3, -1)]
    knight_moves = {}
    for x in range(1, 9):
        for y in range(1, 9):
            pos = (x, y)
            valid_moves = []
            for dx, dy in moves:
                nx, ny = pos[0] + dx, pos[1] + dy
                if 1 <= nx <= 8 and 1 <= ny <= 8:
                    valid_moves.append(coor_to_state((nx, ny)))
            knight_moves[coor_to_state(pos)] = valid_moves
    return knight_moves


def initialize_transition_matrix(knight_moves):
    transition_matrix = np.zeros((64, 64))
    for state, moves in knight_moves.items():
        for move in moves:
            transition_matrix[state, move] = 1 / len(moves)
    return transition_matrix


def compute_expected_time(transition_matrix):
    present = np.zeros(64)
    present[0] = 1
    ans = 0

    for t in range(1, 10002):
        present = np.dot(transition_matrix, present)
        ans += t * present[0]
        transition_matrix[:, 0] = 0  
        if np.all(present < 1e-10):  
            break

    return ans


knight_moves = precompute_knight_moves()
transition_matrix = initialize_transition_matrix(knight_moves)
expected_time = compute_expected_time(transition_matrix)
print(expected_time)
