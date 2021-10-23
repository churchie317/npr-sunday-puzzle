from os import path
import pandas as pd

pd.set_option("display.max_rows", 200, "display.max_columns", 10)


def read_file(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()

        return content.split("\n")


def get_four_letter_words(all_words):
    return filter(lambda word: len(word) == 4, all_words)


def has_one_vowel(word):
    vowels = ["a", "e", "i", "o", "u"]
    word_vowels = "".join(char for char in word if char.lower() in vowels)

    if len(word_vowels) == 1:
        return True
    else:
        return False


def get_celebrities_df():
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, "./celebrities.txt")

    celebrities_df = pd.read_csv(abs_path, header=None, names=["initials", "name"])
    celebrities_df[
        ["first_name", "last_name", "x", "y"]
    ] = celebrities_df.name.str.split(expand=True)
    celebrities_df.drop(["x", "y"], axis=1, inplace=True)

    celebrities_df["last_name"] = celebrities_df["last_name"].str.lower()
    celebrities_df["first_name"] = celebrities_df["first_name"].str.lower()

    return celebrities_df


def run():
    all_words = read_file("./words_alpha.txt")
    eight_letter_words = get_four_letter_words(all_words)
    four_letter_words_one_vowel = set(filter(has_one_vowel, eight_letter_words))

    celebrities_df = get_celebrities_df()

    celebrities_with_four_letter_last_names_df = celebrities_df[
        celebrities_df["last_name"].isin(four_letter_words_one_vowel)
    ]

    celebrities_with_eight_letter_first_names_df = (
        celebrities_with_four_letter_last_names_df[
            celebrities_with_four_letter_last_names_df["first_name"].str.len() == 8
        ]
    )

    print(celebrities_with_eight_letter_first_names_df[["first_name", "last_name"]])
    # for q in four_letter_words_one_vowel:
    #     print(q)


if __name__ == "__main__":
    run()
