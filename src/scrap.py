from pytube import Playlist, YouTube
import json
import whisper


def get_urls():
    """
    Retrieves video URLs from a specific YouTube playlist.

    Parameters:
    None

    Returns:
    list: A list of URLs of videos in the playlist.
    """
    URL_PLAYLIST = (
        "https://www.youtube.com/playlist?list=PLXizq1Vk0pp9WzRhxLGfxnEuC7MFflZHb"
    )
    playlist = Playlist(URL_PLAYLIST)
    print(f"Number of videos in playlist: {len(playlist.video_urls)}")
    urls = [url for url in playlist]
    return urls


def get_captions_from_audio(video_id):
    """
    Generates captions from audio of a given video using the Whisper library.

    Parameters:
    video_id (str): The ID of the YouTube video for which captions are generated.

    Returns:
    None
    """
    model = whisper.load_model("large-v2")
    captions = model.transcribe(f"data/audio/{video_id}.mp4")
    transcription_file_timecode = f"data/transcription/{video_id}_timecodes.txt"
    transcription_file = f"data/transcription/{video_id}.txt"
    with open(transcription_file_timecode, "w", encoding="utf-8") as f:
        for segment in captions["segments"]:
            start_time = timecode_managing(segment["start"])
            end_time = timecode_managing(segment["end"])
            f.write(f"{start_time} - {end_time}: {segment['text']}\n")
    with open(transcription_file, "w", encoding="utf-8") as f:
        for segment in captions["segments"]:
            f.write(f"{segment['text']}\n")


def timecode_managing(seconds):
    """
    Formats timecodes from seconds to HH:MM:SS.

    Parameters:
    seconds (float): Time duration in seconds.

    Returns:
    str: Timecode in HH:MM:SS format.
    """
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def download_video(url):
    """
    Downloads a video from a given URL, extracts its audio, and generates metadata and captions.

    Parameters:
    url (str): The URL of the YouTube video to download.

    Returns:
    None
    """
    vid = YouTube(url)
    audio = vid.streams.get_audio_only()
    audio.download(output_path="data/audio", filename=f"{vid.video_id}.mp4")
    infos = {
        "id": vid.video_id,
        "path": f"data/{vid.video_id}.mp4",
        "transcription_file": f"data/transcription/{vid.video_id}.txt",
        "author": vid.author,
        "channel_id": vid.channel_id,
        "length": vid.length,
        "publish_date": str(vid.publish_date),
        "title": vid.title,
        "views": vid.views,
    }
    with open(f"data/metadata/{vid.video_id}.json", "w") as metadata_file:
        json.dump(infos, metadata_file)
    get_captions_from_audio(vid.video_id)


def main():
    """
    Main function to download videos from a playlist and generate metadata and captions.

    Parameters:
    None

    Returns:
    None
    """
    urls_list = get_urls()
    for url in urls_list:
        download_video(url)


if __name__ == "__main__":
    main()

