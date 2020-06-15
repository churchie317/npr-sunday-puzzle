from os import path
from nltk import corpus, download
from progress.bar import Bar

download("cmudict", quiet=True)
arpabet = corpus.cmudict.dict()


def is_invalid_word(phonemes_set, word_phones_set):
    return (
        len(phonemes_set.intersection(word_phones_set)) > 0 or len(word_phones_set) == 0
    )


def create_new_words(word):
    words = []
    for j in range(3):
        first_char = chr(ord(word[0]) + j)
        base_word = word[1:]
        new_word = f"{first_char}{base_word}"
        words.append(new_word)

    return words


def get_word_phones(word):
    word_phones_set = set()
    pronunciations = arpabet.get(word, [[]])

    for phones in pronunciations:
        for phone in phones:
            word_phones_set.add(phone)

    return word_phones_set


def get_words(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()
        return set([text.lower() for text in content.split("\n") if len(text) == 5])


def run():
    results = []

    words_set = get_words("./words_alpha.txt")
    with Bar("Processing", max=len(words_set)) as bar:
        for word in words_set:
            bar.next()

            matches = []
            phonemes_set = set()

            new_words = create_new_words(word)

            for i in range(len(new_words)):
                new_word = new_words[i]
                word_phones_set = get_word_phones(new_word)

                if (
                    new_word not in words_set
                    or len(word_phones_set) == 0
                    or len(phonemes_set.intersection(word_phones_set)) > 0
                ):
                    break

                phonemes_set.update(word_phones_set)
                matches.append(new_word)

                if i == 2:
                    results.append(matches)

    for matches in results:
        print(f"{matches[0]}, {matches[1]}, {matches[2]}")


if __name__ == "__main__":
    run()
