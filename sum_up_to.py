#!/urs/bin/env python3

def sum_up_to(n):
    if n == 1:
        return 1
    else:
        return n + sum_up_to(n - 1)

print(sum_up_to(10))
