import time
import webbrowser

i = 0
while i < 3:
    time.sleep(2 * 60 * 60)
    webbrowser.open("https://www.youtube.com/watch?v=UmQm76wFfKk")
    i += 1
