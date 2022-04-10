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

    def get_mp3s_by_artist(self, artist):
        output = []
        for t in self.tracks.values():
            if artist in t.artists:
                output.append(t)
        return output


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
