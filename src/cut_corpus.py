import librosa

def load_transcript(transcript_path):
    """
    Load transcript from a text file.

    Parameters:
    transcript_path (str): Path to the transcript file.

    Returns:
    list: List of lines in the transcript file.
    """
    with open(transcript_path, "r") as text:
        return text.readlines()

def load_sound(sound_path):
    """
    Load audio file using librosa.

    Parameters:
    sound_path (str): Path to the audio file.

    Returns:
    tuple: A tuple containing the audio signal and the sample rate.
    """
    y, sr = librosa.load(sound_path, sr=None)
    return y, sr

def cut_sound(sound, sr, start, end):
    """
    Cut a portion of the audio.

    Parameters:
    sound (np.ndarray): Audio signal.
    sr (int): Sample rate.
    start (float): Start time of the segment (in seconds).
    end (float): End time of the segment (in seconds).

    Returns:
    tuple: A tuple containing the cut audio signal and the sample rate.
    """
    start_sample = int(start * sr)
    end_sample = int(end * sr)
    y_cut = sound[start_sample:end_sample]
    return y_cut, sr

def write_transcript(name, number, content):
    """
    Write transcript content to a file.

    Parameters:
    name (str): Name of the file.
    number (int): Number associated with the transcript.
    content (str): Content of the transcript.
    """
    with open(f"4_seconds/{name}_{number}.txt", "w") as file:
        file.write(content)
    
def cut_sound_and_transcript(path):
    """
    Cut audio segments and associated transcripts.

    Parameters:
    path (str): Path to the audio file.

    """
    transcript = load_transcript(path)
    name = "seconds/{path}.txt"
    for i, line in enumerate(transcript):
        number = i
        time = line.split(":")[0].strip()
        sentence = line.split(":")[1]
        start = int(time.split('-')[0].split(":")[-1])
        end = int(time.split("_")[1].split(":")[-1])
        y, sr = load_sound(f"{path}")
        sound_cut, sr = cut_sound(y, sr, start, end)
        librosa.output.write_wav(f'seconds/{name}_{number}.wav', sound_cut, sr)
        write_transcript(name, number, line)

