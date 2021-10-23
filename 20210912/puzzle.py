from os import path
import pandas as pd

pd.set_option("display.max_rows", 1000, "display.max_columns", 10)


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

    return celebrities_df[["first_name", "last_name"]]


def run():
    celebrities_df = get_celebrities_df()

    celebrities_with_five_letter_first_names_df = celebrities_df[
        celebrities_df["first_name"].str.len() == 5
    ]

    celebrities_with_five_letter_first_names_df["rank"] = (
        celebrities_with_five_letter_first_names_df[["first_name", "last_name"]]
        .groupby("first_name")
        .rank(method="first")
    )

    celebrities_with_same_names = celebrities_with_five_letter_first_names_df[
        celebrities_with_five_letter_first_names_df["rank"] > 1
    ]["first_name"].drop_duplicates()

    celebrities_df = pd.merge(
        celebrities_df, celebrities_with_same_names, on="first_name"
    )

    print(celebrities_df[["first_name", "last_name"]])


if __name__ == "__main__":
    run()
