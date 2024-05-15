"""
This module takes a directory of json files and creates the corresponding csv.
Usage:
python3 create_csv.py data/metadata
"""

import sys
import pandas as pd
import glob
import json


def create_dataframe(metadata):
    """
    Creates a DataFrame from a list of json files.

    Parameters:
    metadata (list): A list of file paths (str) pointing to JSON files.

    Returns:
    pd.DataFrame: A DataFrame containing the data extracted from JSON files.
    """
    data = []
    for file in metadata:
        with open(file, "r") as f:
            data.append(json.load(f))
    df = pd.DataFrame(data)
    transcription_files = df["transcription_file"]
    all_transcriptions = []
    for transcription in transcription_files:
        with open(transcription, "r") as text:
            all_transcriptions.append(text.read())
    df["transcription"] = all_transcriptions
    return df


def main():
    """
    Main function to execute the script.

    Parameters:
    None

    Returns:
    None
    """
    metadata = glob.glob(f"{sys.argv[1]}/*.json")
    df = create_dataframe(metadata)
    print(df)
    df.to_csv("metadata_+_transcription.csv", sep="|")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Il faut un dossier avec des fichiers json en argument.")
    main()
