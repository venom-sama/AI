def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        return None

    solutions = []
    for row in board:
        solutions.append(["Q" if cell == 1 else "." for cell in row])

    return solutions

def print_solution(solution):
    if solution is None:
        print("No solution exists.")
    else:
        for row in solution:
            print(" ".join(row))

def main():
    while True:
        print("\nN-Queens Problem Menu:")
        print("1. Solve N-Queens")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the board size (N): "))
            solution = solve_n_queens(n)
            print("\nSolution:")
            print_solution(solution)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
