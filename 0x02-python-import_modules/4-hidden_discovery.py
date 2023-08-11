#!/usr/bin/python3
if __name__ == "__main__":
    import struct
    with open("hidden_4.pyc", mode="rb") as file:
        fileContent = file.read()
        print(fileContent[20:-4])
