import sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:b:c:")
    except getopt.GetoptError:
        print('sysargv.py -a <item> -b <item> -c <item>')
        sys.exit(2)

    for (opt, arg) in opts:

        if opt == '-h':
            print('sysargv.py -a <item> -b <item> -c <item>')
            sys.exit()
        else:
            print("Opt: {}, Arg: {}".format(opt, arg))


if __name__ == '__main__':
    main(sys.argv[1:])