import re
from typing import List
from scipy.interpolate import make_interp_spline
import numpy as np


def tokenize(text: str) -> List[str]:
    return [
        token.lower().replace("’", "'")
        for token in re.findall(r"\b\w+?\b(?:'|’)?", text)
    ]

def percentify(value, max):
    return round(value / max * 100)


def smoothify(yInput, depth):
    x = np.array(range(0, depth))
    y = np.array(yInput)
    # define x as 600 equally spaced values between the min and max of original x
    x_smooth = np.linspace(x.min(), x.max(), 600) 
    # define spline with degree k=3, which determines the amount of wiggle
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    # Return the x and y axis
    return x_smooth, y_smooth

def get_total_string(dataframe):
    transcriptions = dataframe["transcription"].to_list()
    string = ""
    for trans in transcriptions:
        string += trans
    return string
