from os import path
from nltk import corpus, download

download("cmudict", quiet=True)
arpabet = corpus.cmudict.dict()


def is_invalid_word(phonemes_set, word_phones_set):
    return (
        len(phonemes_set.intersection(word_phones_set)) > 0 or len(word_phones_set) == 0
    )


def get_associated_words(word):
    return [f"{chr(ord(word[0]) + j)}{word[1:]}" for j in range(3)]


def get_word_phones(word):
    return {phone for phones in arpabet.get(word, [[]]) for phone in phones}


def get_words(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()
        return set([text.lower() for text in content.split("\n") if len(text) == 5])


def run():
    words_set = get_words("./words_alpha.txt")
    for word in words_set:
        matches = []
        phonemes_set = set()

        for i, new_word in enumerate(get_associated_words(word)):
            word_phones_set = get_word_phones(new_word)

            if new_word not in words_set or is_invalid_word(
                phonemes_set, word_phones_set
            ):
                break

            phonemes_set.update(word_phones_set)
            matches.append(new_word)

            if i == 2:
                print(f"{matches[0]},{matches[1]},{matches[2]}")
                return


if __name__ == "__main__":
    run()
