#!/usr/bin/env python3

import sys

data = sys.stdin.readlines()
format_data = []
padding = 0

for line in data:
    tokens = line.split()
    if len(tokens) == 10:
        format_data.append(tokens)
        if len(tokens[1]) > padding:
            padding = len(tokens[1])
    else:
        team_len = len(tokens) - 9  # find length of name and extract it
        team = ""
        for i in range(team_len):  # add formatted name in new list
            team += f"{tokens[1 + i]} "
        team = team[:-1]  # remove last whitespace
        format_data.append(tokens[:1] + [team] + tokens[team_len + 1:])
        if len(team) > padding:
            padding = len(team)

print(f"POS CLUB{' ' * (padding - 4)}  P   W   D   L  GF  GA  GD PTS")

for line in format_data:
    [pos, club, p, w, d, l, gf, ga, gd, pts] = line
    print(f"{pos:>3} {club:{padding}} {p:>2} {w:>3} {d:>3} {l:>3} {gf:>3} {ga:>3} {gd:>3} {pts:>3}")
