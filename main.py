from pytube import YouTube
import sys


def process(youtube_url: str = None):
    print(f"Will process '{youtube_url}'")
    yt = YouTube(youtube_url)
    print("Downloading ...")
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
        output_path="download")
    print("Done.")


if __name__ == '__main__' and len(sys.argv) > 1:
    process(sys.argv[1])
