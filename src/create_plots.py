import matplotlib.pyplot as plt
import pandas as pd
import sys
import glob
import numpy as np

from create_csv import create_dataframe
from utils import tokenize

def plot_nb_tokens_transcr(data):
    transcriptions = data["transcription"].tolist()
    data["nb_tokens"] = [len(tokenize(transcription)) for transcription in transcriptions]
    plt.bar(np.arange(len(data)), np.array(data["nb_tokens"]), color ='maroon', width = 0.4)
    plt.xlabel("Video index")
    plt.ylabel("Nombre de tokens dans la transcription")
    plt.title("Nombre de tokens par video")
    plt.show()

def plot_views_on_length(data):
    data = data[["views", "length"]].sort_values(by=["length"])
    views = np.array(data["views"])
    length = np.array(data["length"])
    plt.plot(length, views)
    plt.title("Nombre de vues en fonction de la longueur de la video")
    plt.xlabel("Longueur de la video")
    plt.ylabel("Nombre de vues")
    plt.show()

def main():
    if len(sys.argv) != 2:
        sys.exit("Il faut le dossier `data` en argument.")
    json_files = glob.glob(f"{sys.argv[1]}/metadata/*.json")
    json_data = create_dataframe(json_files)
    # print(json_data)
    # plot_views_on_length(json_data)
    plot_nb_tokens_transcr(json_data)

if __name__ == "__main__":
    main()
