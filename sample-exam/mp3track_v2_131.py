#!/usr/bin/env python3

class MP3Track(object):

    def __init__(self, title, duration, artists=None):
        self.title = title
        self.duration = duration
        self.artists = [] if artists is None else artists

    def __str__(self):
        output = []
        output.append(f"Title: {self.title}")
        output.append(f"By: {', '.join(self.artists)}")
        output.append(f"Duration: {self.duration}")
        return "\n".join(output)


def main():
    pass


if __name__ == "__main__":
    main()
