from pytube import Playlist, YouTube, Caption 
import json


def get_urls():
    URL_PLAYLIST = (
        "https://www.youtube.com/playlist?list=PLXizq1Vk0pp9WzRhxLGfxnEuC7MFflZHb"
    )
    playlist = Playlist(URL_PLAYLIST)
    print(f"Number of videos in playlist: {len(playlist.video_urls)}")
    urls = [url for url in playlist]
    return urls


def download_video(url):
    vid = YouTube(url)

    print(f"Author : {vid.author}")
    print(f"Channel_id: {vid.channel_id}")
    print(f"Length: {vid.length}s")
    print(f"Publish date: {vid.publish_date}")
    print(f"Title: {vid.title}")
    print(f"Views: {vid.views}")
    audio = vid.streams.get_audio_only()
    audio.download(output_path="data/audio", filename=f"{vid.video_id}.mp4")
    infos = {"id": vid.video_id, "path": f"data/{vid.video_id}.mp4", "sentences": None, "author": vid.author, "channel_id": vid.channel_id, "length": vid.length, "publish_date": str(vid.publish_date), "title": vid.title, "views": vid.views}
    with open(f"data/metadata/{vid.video_id}.json", "w") as metadata_file:
        json.dump(infos, metadata_file)


def main():
    urls_list = get_urls()
    for url in urls_list:
        download_video(url)


if __name__ == "__main__":
    main()
