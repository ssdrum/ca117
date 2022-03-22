#!/usr/bin/env python3

class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {"swim": None, "cycle": None, "run": None}

    def __str__(self):
        output = []
        output.append(f"Name: {self.name}")
        output.append(f"ID: {self.tid}")
        output.append(f"Race time: {sum(self.times.values())}")
        return "\n".join(output)

    def add_time(self, disc, time):  # short for discipline
        self.times[disc] = time

    def get_time(self, disc):
        return f"{self.times[disc]}"


def main():
    pass


if __name__ == "__main__":
    main()
