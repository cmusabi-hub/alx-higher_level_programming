#!/usr/bin/python3
import hidden_4

def main():
    direc = dir(hidden_4)
    for mod_ in direc:
        if mod_[0:2] == "__":
            continue
        else:
            print("{}".format(mod_))


if __name__ == "__main__":
    main()
