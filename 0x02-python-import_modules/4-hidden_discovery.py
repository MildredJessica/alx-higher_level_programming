#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all the names defined by the module hidden_4"""
    import hidden_4

    for name in dir(hidden_4):
        if name[:2] != "__":
            print("{}".format(name))
