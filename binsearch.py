#!/usr/bin/env python3

def binSearch(query, sortedList):
    low = 0
    high = len(sortedList) - 1

    while low <= high:
        mid = (low + high) // 2

        if sortedList[mid] < query:
            low = mid + 1

        elif sortedList[mid] > query:
            high = mid - 1

        else:
            return True

    return False

def main():
    pass


if __name__ == "__main__":
    main()