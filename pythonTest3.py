#!/usr/bin/env python3

print("Type integers, each followed by Enter; or just Enter to finsih")


def get_numbers():
    total = 0
    count = 0

    while True:
        line = input("integer: ")
        if line:
            try:
                number = int(line)
            except ValueError as err:
                print(err)
                continue
            total += number
            count += 1
        else:
            break
    return (count, total)


(count, total) = get_numbers()

if count:
    print("count =", count, "total =", total, "mean =", total / count)
