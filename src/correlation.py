"""
This script analyzes the correlation between the length of transcriptions and the number of tokens.
It reads JSON files containing transcriptions, calculates the number of tokens in each transcription,
and then calculates the correlation between the length of transcriptions and the number of tokens.
"""


import numpy as np
import sys
import pandas as pd
import glob
from scipy.stats import pearsonr

from create_csv import create_dataframe
from utils import tokenize


def calculate_correlation(data):
    """
    Calculate Pearson correlation coefficient between the length of transcriptions 
    and the number of tokens in each transcription.

    Parameters:
    data (DataFrame): A pandas DataFrame containing columns "nb_tokens" and "length".

    Returns:
    tuple: A tuple containing the Pearson correlation coefficient and the p-value.
    """
    data = data[["nb_tokens", "length"]].sort_values(by=["length"])
    nb_tokens = np.array(data["nb_tokens"])
    length = np.array(data["length"])
    correlation_matrix = pearsonr(length, nb_tokens)
    return correlation_matrix


def main():
    """
    Entry point of the script. Reads JSON files containing transcriptions,
    calculates the number of tokens in each transcription, and then calculates
    the correlation between the length of transcriptions and the number of tokens.
    Prints the correlation coefficient.
    """
    if len(sys.argv) != 2:
        sys.exit("Il faut le dossier `data` en argument.")
    json_files = glob.glob(f"{sys.argv[1]}/metadata/*.json")
    json_data = create_dataframe(json_files)
    transcriptions = json_data["transcription"].tolist()
    json_data["nb_tokens"] = [
        len(tokenize(transcription)) for transcription in transcriptions
    ]
    correlation = calculate_correlation(json_data)
    print(correlation)


if __name__ == "__main__":
    main()
