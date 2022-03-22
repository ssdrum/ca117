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
        output.append(f"Race time: {self.get_tot_time()}")
        return "\n".join(output)

    def add_time(self, disc, time):  # short for discipline
        self.times[disc] = time

    def get_time(self, disc):
        return f"{self.times[disc]}"

    def get_tot_time(self):
        return sum(self.times.values())

    def __eq__(self, other):
        return self.get_tot_time() == other.get_tot_time()

    def __lt__(self, other):
        return self.get_tot_time() < other.get_tot_time()

    def __gt__(self, other):
        return self.get_tot_time() > other.get_tot_time()


class Triathlon(object):

    def __init__(self):
        self.triathletes = {}

    def add(self, t):
        self.triathletes[t.tid] = t

    def remove(self, tid):
        if tid in self.triathletes:
            del self.triathletes[tid]

    def lookup(self, tid):
        return self.triathletes[tid] if tid in self.triathletes else None

    def __str__(self):
        output = []
        tokens = [[self.triathletes[t].name, self.triathletes[t].tid] for t in self.triathletes]  # makes list of lists [name, tid]
        tokens.sort(key=lambda list: list[0])  # sort list of lists by name
        for t in tokens:
            output.append(f"Name: {t[0]}\nID: {t[1]}")

        return "\n".join(output)


def main():
    pass


if __name__ == "__main__":
    main()
