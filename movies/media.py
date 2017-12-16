import webbrowser


class Movie:
    """This is a movie class"""

    VALID_RATINGS = ["G", "PG", "PG13", "R", "NC-17"]

    def __init__(self, title, storyline, poster_url, trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def __str__(self):
        return self.title + "\n" + self.storyline + "\n" + self.poster_image_url + "\n" + self.trailer_youtube_url



