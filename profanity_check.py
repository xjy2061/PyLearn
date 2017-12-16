import urllib.request
import urllib.parse


def read_check():
    stream = open(r"movie_quotes")
    content = stream.read()
    print(content)
    profanity_check(content)
    stream.close()


def profanity_check(text):
    print("============")
    response = urllib.request.urlopen("http://www.wdylike.appspot.com/?" + urllib.parse.urlencode({"q" : text}))
    if response.read() == b"true":
        print("Alarm!!!")
    else:
        print("Clear.")
    response.close()


read_check()
