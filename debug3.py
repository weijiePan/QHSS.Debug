# debug3.py

# This script asks the user to enter a list of words separated by commas,
# then checks if the list is a palindrome (reads the same forwards and backwards).

# Normalize words (lowercase and strip spaces), then check if they form a palindrome.
def is_palindrome(items: list[str]):
    cleaned = [item.casefold().strip() for item in items]
    print(cleaned)
    for i in range(len(cleaned) // 2):
        print(cleaned[i], cleaned[~i])
        if cleaned[i] != cleaned[~i]:
            return False
    return True

# Prompt the user for input and split it into a list of words.
def get_input_list() -> list[str]:
    line = input("Enter a list of words separated by commas: ")
    return line.split(",")

# Main function that controls input, checking, and output.
def main() -> None:
    items: list[str] = get_input_list()
    if is_palindrome(items):
        print("The list is a palindrome!")
    else:
        print("The list is not a palindrome.")

main()
