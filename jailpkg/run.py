import sys
import argparse
import yaml
"""Simple scripts for managing packages in jails"""

def generate_command(package, jailpath, additional_args=None):
    """Generate raw command to be run to install packages"""
    if additional_args is None: additional_args = ''
    command = "pkg install %s -c %s %s" % (package, jailpath, additional_args)
    return command

def parse_yaml_packages(filename):
    """Get a list of package names from yaml file"""
    packagesdict = {}
    with open(filename, 'r') as stream:
        packagesdict = yaml.load(stream)
    return packagesdict

def main():
    p = argparse.ArgumentParser(description='Simple script for managing packages in jails')
    p.add_argument('-p', '--package', dest='package', 
            help='name of package to install')
    p.add_argument('-j', '--jailpath', dest='jailpath',
            help='full path to jail to install package in')
    args = p.parse_args()

    # Not going to validate these - we'll be passing errors back from pkgng
    # anyway.
    package = args.package
    jailpath = args.jailpath
    command = generate_command(package, jailpath)
    print command
