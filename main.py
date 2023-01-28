from pytube import YouTube


def process():
    yt = YouTube('https://www.youtube.com/watch?v=dduIj3lAZk0')
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
