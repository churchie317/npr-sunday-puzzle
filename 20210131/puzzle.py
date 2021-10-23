from itertools import groupby
from os import path


def read_file(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()

        return content.split("\n")


def get_eight_letter_words():
    all_words = read_file("./words_alpha.txt")
    sorted_eight_letter_words = sorted(
        map(
            lambda word: {"sorted": "".join(sorted(word)), "source": word},
            all_words,
        ),
        key=lambda word: word["sorted"],
    )

    return {
        k: list(map(lambda word: word["source"], g))
        for k, g in groupby(sorted_eight_letter_words, key=lambda word: word["sorted"])
    }


def get_states():
    all_states = read_file("./states.txt")
    return {states.split(",")[0]: states.split(",")[1:] for states in all_states}


def get_state_combinations(state, states_map, previous_states, size):
    visited_states = [*previous_states, state]

    unvisited_adjacent_states = set.difference(
        set(states_map[state]), set(visited_states)
    )

    if len(visited_states) == size:
        return ["".join(visited_states)]

    if len(unvisited_adjacent_states) == 0:
        return ["".join(visited_states)]

    adjacent_states = states_map[state]

    combinations = []
    for adjacent_state in unvisited_adjacent_states:
        combinations += get_state_combinations(
            adjacent_state, states_map, visited_states, size
        )

    return combinations


def run():
    eight_letter_words = get_eight_letter_words()
    states_map = get_states()

    for (state, adjacent_states) in states_map.items():
        trip = get_state_combinations(state, states_map, set(), 7)
        normalized_trips = map(lambda word: ("".join(sorted(word)), word), trip)
        for normalized_trip in normalized_trips:
            if normalized_trip[0] in eight_letter_words:
                print(f"{normalized_trip[1]}: {eight_letter_words[normalized_trip[0]]}")


if __name__ == "__main__":
    run()
