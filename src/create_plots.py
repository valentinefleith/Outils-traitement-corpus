import matplotlib.pyplot as plt
import pandas as pd
import sys
from create_csv import create_dataframe
import glob
import numpy as np

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
    print(json_data)
    plot_views_on_length(json_data)

if __name__ == "__main__":
    main()
