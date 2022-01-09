from pywebio.input import TIME, input, TEXT
from pywebio.output import OutputPosition, output, put_code, put_image, put_loading, put_text
from pytube import YouTube
def blinc():
    for color in ('danger', 'warning', 'info'):
        put_loading(shape='grow', color=color)
def bmi():
    name = input("Copy link here ")
    return name
def ytfun():
    video_list=[bmi()]
    for i in video_list:
        try:
            yt=YouTube(i)
            blinc()
            put_text("Downloading the Link:  "+i)
            put_code("hello",position= 'middle')
            put_text("Downloading the Video:  "+ yt.streams[0].title)
            put_image(yt.thumbnail_url,width='710',height='405')
        except Exception as e:
            print("ERORR~~")
        stream = yt.streams.filter(res="144p").first()
        stream.download("Downloads/")
        put_text("Task Completed Downloded---")
if __name__ == '__main__':
    ytfun()
