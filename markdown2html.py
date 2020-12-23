#!/usr/bin/python3
""" Start a script
    """

import sys
import os


def markdownhtml():
    """ that takes an argument 2 strings
    """
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)
    else:
        file_start = sys.argv[1]
        file_out = sys.argv[2]
        if os.path.isfile(file_start):
            sys.exit(0)
        else:
            print("Missing {}".format(file_start), file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    markdownhtml()
