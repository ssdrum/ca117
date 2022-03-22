#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"


class Schedule(object):

    def __init__(self, meetings=None):
        self.meetings = {} if meetings is None else meetings

    def add(self, m):  # using the __str__ method return value as key
        self.meetings[m.__str__()] = m

    def __str__(self):
        output = ["Schedule", "--------"]
        for m in sorted(self.meetings):
            output.append(self.meetings[m].__str__())
        output.append(f"Meetings today: {len(self.meetings)}")
        return "\n".join(output)


def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)


if __name__ == "__main__":
    main()
