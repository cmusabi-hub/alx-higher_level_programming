#!/usr/bin/python3


def main():
    import hidden_4

    direc = dir(hidden_4)
    for mod in direc:
        if mod[0:2] != "__":
            print(mod)


if __name__ == "__main__":
    main()
