#!/usr/bin/python3


def main():
    import hidden_4
    direc = dir(hidden_4)
    for i in range(len(direc)):
        if direc[0:2] != "__":
            print(direc)


if __name__ == "__main__":
    main()
