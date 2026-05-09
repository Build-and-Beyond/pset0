"""
MORSE - Convert text into Morse code.

Implement a program that prompts the user for a word or sentence
and outputs the corresponding Morse code representation.

Letters should be separated by spaces. Words (spaces in input) should
be separated by " / ".

Morse code dictionary:
    A: .-      B: -...    C: -.-.    D: -..     E: .
    F: ..-.    G: --.     H: ....    I: ..      J: .---
    K: -.-     L: .-..    M: --      N: -.      O: ---
    P: .--.    Q: --.-    R: .-.     S: ...     T: -
    U: ..-     V: ...-    W: .--     X: -..-    Y: -.--
    Z: --..
    0: -----   1: .----   2: ..---   3: ...--   4: ....-
    5: .....   6: -....   7: --...   8: ---..   9: ----.

Example:
    Input: SOS
    Output: ... --- ...

    Input: HELLO
    Output: .... . .-.. .-.. ---
"""

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/",
}


def main():
    # TODO: Prompt the user for a word or sentence
    # TODO: Convert each character to its Morse code representation
    # TODO: Print the result with spaces between letters
    pass


if __name__ == "__main__":
    main()