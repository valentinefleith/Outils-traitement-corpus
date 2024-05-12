import re
from typing import List
from scipy.interpolate import make_interp_spline
import numpy as np

def tokenize(text: str) -> List[str]:
    """
    Tokenize the input text into a list of words.

    Parameters:
    - text (str): The input text to be tokenized.

    Returns:
    - List[str]: A list of tokens (words) extracted from the input text.
    """
    return [
        token.lower().replace("’", "'")
        for token in re.findall(r"\b\w+?\b(?:'|’)?", text)
    ]

def percentify(value, max):
    """
    Convert a value to a percentage of the maximum value.

    Parameters:
    - value: The value to be converted to a percentage.
    - max: The maximum value.

    Returns:
    - float: The value as a percentage of the maximum value.
    """
    return round(value / max * 100)

def smoothify(yInput, depth):
    """
    Smoothify a set of data points using cubic spline interpolation.

    Parameters:
    - yInput: The input data points.
    - depth: The depth of the data points.

    Returns:
    - Tuple[np.ndarray, np.ndarray]: A tuple containing the smoothed x and y data points.
    """
    x = np.array(range(0, depth))
    y = np.array(yInput)
    x_smooth = np.linspace(x.min(), x.max(), 600) 
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_smooth)
    return x_smooth, y_smooth

def get_total_string(dataframe):
    """
    Concatenate all transcriptions in a DataFrame into a single string.

    Parameters:
    - dataframe: The DataFrame containing transcriptions.

    Returns:
    - str: A single string containing all transcriptions concatenated.
    """
    transcriptions = dataframe["transcription"].to_list()
    string = ""
    for trans in transcriptions:
        string += trans
    return string

