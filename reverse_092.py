#!/usr/bin/env python3

def reverse_list(l):
    if len(l) == 1:
        return l
    else:
        return reverse_list(l[:-1])


def main():
    print(reverse_list([1,2,3]))
    print(reverse_list([3,4,5,6]))
    print(reverse_list([1,2]))


if __name__ == "__main__":
    main()
