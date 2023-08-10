#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    lenght = len(sys.argv) - 1
    result = 0
    for i in range(lenght):
        result += int(args[i])

    print(result)
