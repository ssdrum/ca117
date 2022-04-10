#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artists=None):
        self.title = title
        self.duration = duration
        self.artists = [] if artists is None else artists

    def add_artist(self, artist):
        self.artists.append(artist)

    def __str__(self):
        output = []
        output.append(f"Title: {self.title}")
        output.append(f"By: {', '.join(self.artists)}")
        minutes = self.duration // 60
        seconds = self.duration % 60
        output.append(f"Duration: {minutes}:{seconds:02d}")
        return "\n".join(output)


def main():
    pass


if __name__ == "__main__":
    main()
