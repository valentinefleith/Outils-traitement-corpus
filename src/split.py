"""
This script splits a dataset into a train set and a validation/test set using train_test_split from sklearn.
It reads JSON files containing transcriptions, calculates the number of tokens in each transcription,
and then splits the data into train and validation/test sets. The train set contains 75% of the data,
and the validation/test set contains 25%.
"""


import sys
from sklearn.model_selection import train_test_split
import pandas as pd
import glob
from create_csv import create_dataframe
from utils import tokenize


def main():
    """
    Split the dataset into train and validation/test sets.

    Reads JSON files containing transcriptions, calculates the number of tokens in each transcription,
    and then splits the data into train and validation/test sets using train_test_split from sklearn.

    Prints the train and validation/test sets.

    The train set contains 75% of the data, and the validation/test set contains 25%.
    """
    if len(sys.argv) != 2:
        sys.exit("A folder name must be provided as an argument.")
    json_files = glob.glob(f"{sys.argv[1]}/metadata/*.json")
    json_data = create_dataframe(json_files)
    transcriptions = json_data["transcription"].tolist()
    json_data["nb_tokens"] = [
        len(tokenize(transcription)) for transcription in transcriptions
    ]
    train_set, validation_test_set = train_test_split(
        json_data, test_size=0.25, random_state=42
    )
    print("Train Set:")
    print(train_set)
    print("\nValidation/Test Set:")
    print(validation_test_set)


if __name__ == "__main__":
    main()
