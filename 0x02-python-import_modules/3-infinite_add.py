#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    if args == 1:
        print("{}".format(args - 1))
    elif args > 1:
        total = 0
        for x in range(1, args):
            total += int(sys.argv[x])
        print ("{}".format(total))
