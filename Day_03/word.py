#this file uses the string_utils.py file to perform basic string functionalities

from string_utils import to_upper, to_lower, count_characters

def main():
    word = input("Enter a word: ")

    upper_word = to_upper(word)
    lower_word = to_lower(word)
    character_count = count_characters(word)

    print(f"Uppercase: {upper_word}")
    print(f"Lowercase: {lower_word}")
    print(f"Character Count: {character_count}")

if __name__ == "__main__":
    main()