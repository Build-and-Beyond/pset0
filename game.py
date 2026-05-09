"""Logic101 PSET 0: Simple Grid Game

Implement the functions below to create a simple grid-based game.
"""

BOARD_SIZE = 5
EMPTY_CELL = "---"


def create_board(size: int = BOARD_SIZE) -> list[list[str]]:
    """Create an empty game board.

    Args:
        size: The size of the board (size x size grid)

    Returns:
        A 2D list representing the game board with empty cells.
    """
    # TODO: Implement this function
    return []


def format_board(board: list[list[str]]) -> str:
    """Format the board as a string for display.

    Args:
        board: The game board

    Returns:
        A string representation of the board with rows on separate lines.
    """
    # TODO: Implement this function
    return ""


def validate_input(user_input: str, size: int = BOARD_SIZE) -> bool:
    """Validate user input for a move.

    Args:
        user_input: The user's input string (e.g., 'A1', 'E5')
        size: The size of the board

    Returns:
        True if the input is valid, False otherwise.
    """
    # TODO: Implement this function
    return False


def place_move(board: list[list[str]], position: str, marker: str = " X ") -> list[list[str]]:
    """Place a move on the board.

    Args:
        board: The game board
        position: The position string (e.g., 'A1')
        marker: The marker to place on the board

    Returns:
        The updated board.
    """
    # TODO: Implement this function
    return board


def main():
    """Main game loop."""
    board = create_board()
    print("Welcome to the Grid Game!")
    print("Enter positions like A1, B3, E5 (row letter + column number)")
    print("Type 'quit' to exit\n")

    while True:
        print(format_board(board))
        user_input = input("Enter your move: ").strip().upper()

        if user_input == "QUIT":
            print("Thanks for playing!")
            break

        if not validate_input(user_input):
            print("Invalid input. Please try again.\n")
            continue

        board = place_move(board, user_input)
        print()


if __name__ == "__main__":
    main()