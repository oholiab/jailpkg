import sys
import os
"""Simple scripts for managing packages in jails"""

def main(args):
    if len(args) < 2:
        sys.stderr.write("Requires at least 2 args\n")
        sys.exit(1)
    name = args[0]
    jailpath = args[1]
    command = "pkg install %s -c %s" % (name, jailpath)
    print command

if __name__ == "__main__":
    main(sys.argv)    
