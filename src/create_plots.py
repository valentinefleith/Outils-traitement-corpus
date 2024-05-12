import matplotlib.pyplot as plt
import pandas as pd
import sys
import glob
import numpy as np
import collections

from create_csv import create_dataframe
from utils import tokenize, smoothify, get_total_string, percentify
from scipy.interpolate import make_interp_spline

def plot_nb_tokens_transcr(data):
    """
    Plot the number of tokens in each transcription.

    Parameters:
    - data (DataFrame): A DataFrame containing video metadata, including the column "nb_tokens" representing the number of tokens in each transcription.

    Returns:
    - None
    """
    plt.bar(np.arange(len(data)), np.array(data["nb_tokens"]), color ='maroon', width = 0.4)
    plt.xlabel("Video index")
    plt.ylabel("Nombre de tokens dans la transcription")
    plt.title("Nombre de tokens par video")
    plt.show()

def plot_views_on_length(data):
    """
    Plot the number of views against the length of the video.

    Parameters:
    - data (DataFrame): A DataFrame containing video metadata, including the columns "views" and "length" representing the number of views and the length of each video, respectively.

    Returns:
    - None
    """
    data = data[["views", "length"]].sort_values(by=["length"])
    views = np.array(data["views"])
    length = np.array(data["length"])
    X_Y_Spline = make_interp_spline(length, views)
    X_ = np.linspace(length.min(), length.max(), 500)
    Y_ = X_Y_Spline(X_)
    plt.plot(X_, Y_)
    plt.title("Nombre de vues en fonction de la longueur de la video")
    plt.xlabel("Longueur de la video")
    plt.ylabel("Nombre de vues")
    plt.show()

def plot_nb_tokens_on_length(data):
    """
    Plot the number of views against the length of the video.

    Parameters:
    - data (DataFrame): A DataFrame containing video metadata, including the columns "nb_tokens" and "length" representing the number of tokens and the length of each video, respectively.

    Returns:
    - None
    """
    data = data[["nb_tokens", "length"]].sort_values(by=["length"])
    nb_tokens = np.array(data["nb_tokens"])
    length = np.array(data["length"])
    X_Y_Spline = make_interp_spline(length, nb_tokens)
    X_ = np.linspace(length.min(), length.max(), 500)
    Y_ = X_Y_Spline(X_)
    plt.plot(X_, Y_)
    plt.title("Nombre de tokens en fonction de la longueur de la video")
    plt.xlabel("Longueur de la video")
    plt.ylabel("Nombre de tokens")
    plt.show()


def plot_zipf(data):
    """
    Plot Zipf's Law based on the transcriptions of the videos.

    Parameters:
    - data (DataFrame): A DataFrame containing video metadata, including the column "transcription" representing the transcriptions of each video.

    Returns:
    - None
    """
    depth = 100
    text = tokenize(get_total_string(data))
    word_frequencies = collections.Counter(text)
    top_word_frequencies = word_frequencies.most_common(depth)
    maxVal = top_word_frequencies[0][1]
    yAxis = [percentify(top_word_frequencies[i][1], maxVal) for i in range(depth)]
    x, y = smoothify(yAxis, depth)
    plt.plot(x, y, label="Corpus", lw=1, alpha=0.5)
    ziffianCurveValues = [100/i for i in range(1, depth+1)]
    x, y = smoothify(ziffianCurveValues, depth)
    plt.plot(x, y, label='Ziffian Curve', ls=':', color='grey')
    plt.legend()
    plt.title("Loi de Zipf a partir des transcriptions du corpus audio")
    plt.show()

def main():
    if len(sys.argv) != 2:
        sys.exit("Il faut le dossier `data` en argument.")
    json_files = glob.glob(f"{sys.argv[1]}/metadata/*.json")
    json_data = create_dataframe(json_files)
    transcriptions = json_data["transcription"].tolist()
    json_data["nb_tokens"] = [len(tokenize(transcription)) for transcription in transcriptions]
    # print(json_data)
    # plot_views_on_length(json_data)
    # plot_nb_tokens_transcr(json_data)
    # plot_zipf(json_data)
    plot_nb_tokens_on_length(json_data)

if __name__ == "__main__":
    main()

