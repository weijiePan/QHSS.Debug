# debug4.py

# This script manually converts a sentence into title case,
# where the first letter of each word is capitalized.

# Take a sentence and convert it to title case without using str.title().
def to_title_case(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) == 0:
            continue
        words[i] = words[i][0].upper() + words[i][1:]
    return " ".join(words)

# Main function to prompt user input and show converted result.
def main():
    print("Title Case Converter")
    user_input = input("Enter a sentence: ")
    result = to_title_case(user_input)
    print("Converted:", result)

main()
