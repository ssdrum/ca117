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


def main():
    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)


if __name__ == "__main__":
    main()
