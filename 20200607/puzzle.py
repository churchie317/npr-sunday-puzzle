from itertools import permutations
import logging
from re import sub
from os import path
import sys


def read_file(rel_file_path):
    abs_dir = path.abspath(path.dirname(__file__))
    abs_path = path.join(abs_dir, rel_file_path)
    with open(abs_path, "r") as data:
        content = data.read()
        return [
            ("".join(sorted(sub("[\W_]+", "", text.lower()))), text)
            for text in content.split("\n")
        ]


def run():
    restaurants_dict = {k: v for (k, v) in read_file("./restaurants.txt")}
    regions = read_file("./us_regions.txt")

    for (region_sorted, region_orig) in regions:
        logging.info(f"checking for word: {region_orig}")
        for region in region_sorted:
            if restaurants_dict.get(region_sorted):
                print(
                    f"Restaurant: {restaurants_dict[region_sorted]}; Region: {region_orig}"
                )
                sys.exit(0)

    exit("not found")


if __name__ == "__main__":
    run()
