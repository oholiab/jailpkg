import sys
import argparse
"""Simple scripts for managing packages in jails"""

def main():
    p = argparse.ArgumentParser(description='Simple script for managing packages in jails')
    p.add_argument('-p', '--package', dest='package', 
            help='name of package to install')
    p.add_argument('-j', '--jailpath', dest='jailpath',
            help='full path to jail to install package in')
    args = p.parse_args()
    package = args.package
    jailpath = args.jailpath
    print args
    command = "pkg install %s -c %s" % (package, jailpath)
    print command

if __name__ == "__main__":
    main()    
