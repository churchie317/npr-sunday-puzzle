from os import path


def read_file(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()

        return content.split("\n")


def get_eight_letter_words():
    all_words = read_file("./words_alpha.txt")
    eight_letter_words = filter(
        lambda word: len(word) == 8 and word[2] == "a" and word[5] == "a", all_words
    )

    return list(eight_letter_words)


def run():
    eight_letter_words = get_eight_letter_words()
    six_letter_words = filter(
        lambda word: len(word) == 6,
        map(lambda word: word.replace("a", ""), eight_letter_words),
    )

    for q in six_letter_words:
        print(q)


if __name__ == "__main__":
    run()
