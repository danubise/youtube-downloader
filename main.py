from pytube import YouTube
import sys
import os


def process(youtube_url: str = None, audio: bool = False):
    print(f"Will process '{youtube_url}'")
    yt = YouTube(youtube_url)
    print("Downloading ...")
    if audio:
        print(f"Audio title '{yt.title}'")
        y_obj = yt.streams.filter(only_audio=audio)
        file_pref = "audio_"
    else:
        file_pref = "video_"
        print(f"Video title '{yt.title}'")
        file_extension = 'mp4'
        y_obj = yt.streams.filter(progressive=True,
                                  file_extension=file_extension).order_by('resolution').desc()
    out_file = y_obj.first().download(
        output_path="download", filename_prefix=file_pref)
    new_file = out_file
    if audio:
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
    new_file = new_file.replace('\"', " ") \
        .replace('|', " ") \
        .replace(',', " ") \
        .replace('/"', " ") \
        .replace('\\', " ") \
        .replace(':', " ") \
        .replace('*"', " ") \
        .replace('?', " ") \
        .replace('<', " ") \
        .replace('>"', " ")
    os.rename(out_file, new_file)
    out_file = new_file
    print(f"File name '{out_file}'")
    print("Done.")


print(sys.argv)
if len(sys.argv) > 1:
    audio = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "audio":
            audio = True

    process(sys.argv[1], audio)
else:
    print("Please provide youtube URL as argument")
