import sys
import argparse
import yaml
"""Simple scripts for managing packages in jails"""

def generate_command(package, jailpath, additional_args=None):
    """Generate raw command to be run to install packages"""
    if additional_args is None: additional_args = ''
    command = "pkg install %s -c %s %s" % (package, jailpath, additional_args)
    return command.rstrip()

def parse_yaml_packages(filename):
    """Get a list of package names from yaml file"""
    packagesdict = {}
    with open(filename, 'r') as stream:
        packagesdict = yaml.load(stream)
    return packagesdict

def yaml_to_commands(configfile):
    """Parse a yaml file to a list of commands"""
    commandlist = []
    config = parse_yaml_packages(configfile)
    for jailpath, packages in config.iteritems():
        for package in packages:
            commandlist.append(generate_command(package, jailpath))
    return commandlist

def parse_args(test_args=None):
    p = argparse.ArgumentParser(description='Simple script for managing packages in jails')
    p.add_argument('-p', '--package', dest='package', 
            help='name of package to install')
    p.add_argument('-j', '--jailpath', dest='jailpath',
            help='full path to jail to install package in')
    p.add_argument('-c', '--config', dest='configfile')
    if not test_args == None:
        args = p.parse_args(test_args)
    else:
        args = p.parse_args()
    if getattr(args, "package") and getattr(args, "configfile"):
        sys.stderr.write("--package and --jailpath args are mutually exclusive to --config\n")
        sys.exit(1)
    if not getattr(args, "configfile") and not all([getattr(args,x) for x in ('package', 'jailpath')]):
        sys.stderr.write("--package and --jailpath arguments must be specified together (or use --config)\n")
        sys.exit(1) 
    return args

def main():
    args = parse_args()

    # Not going to validate these - we'll be passing errors back from pkgng
    # anyway.
    package = args.package
    jailpath = args.jailpath
    command = generate_command(package, jailpath)
    print command
