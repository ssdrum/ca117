#!/usr/bin/env python3


class MP3Collection(object):

    def __init__(self):
        self.tracks = {}

    def add(self, track):
        self.tracks[track.title] = track

    def remove(self, title):
        if title in self.tracks:
            del self.tracks[title]

    def lookup(self, title):
        return self.tracks[title] if title in self.tracks else None


class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        output = []
        output.append(f"Title: {self.title}")
        output.append(f"Duration: {self.duration}")
        return "\n".join(output)


def main():
    pass


if __name__ == "__main__":
    main()
