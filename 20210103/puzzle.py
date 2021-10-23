from os import path
from re import sub
from string import ascii_lowercase


def get_words(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()

        return content.split("\n")


def get_hyphenated_words(words):
    return list(filter(lambda word: "-" in word, words))


def get_seven_letter_words(words):
    return set(filter(lambda word: len(standardize_word(word)) == 7, words))


def standardize_word(word):
    return sub("[\W_]+", "", word.lower())


def run():
    words = get_words("./words.txt")
    seven_letter_words = get_seven_letter_words(words)
    standardized_seven_letter_words_map = {
        standardize_word(word): word for word in seven_letter_words
    }
    hyphenated_seven_letter_words = get_hyphenated_words(seven_letter_words)

    for word in hyphenated_seven_letter_words:
        standardized_word = standardize_word(word)
        candidates = []
        for letter in ascii_lowercase:
            updated_word = standardized_word[0:3] + letter + standardized_word[4:]
            if (
                updated_word != standardized_word
                and updated_word in standardized_seven_letter_words_map
            ):
                candidates.append(standardized_seven_letter_words_map[updated_word])

        if len(candidates) != 0:
            print(f"WORD: {word}; CANDIDATES: {candidates}")


if __name__ == "__main__":
    run()
