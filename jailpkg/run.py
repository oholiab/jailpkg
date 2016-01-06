import sys
import argparse
import yaml
import string
from subprocess import Popen, PIPE
"""Simple scripts for managing packages in jails"""

class ArgumentError(ValueError):
    pass

def generate_command(package, jailpath, additional_args=None):
    """Generate raw command to be run to install packages"""
    if additional_args is None: additional_args = ''
    command = "pkg -c %s install --yes %s" % (jailpath, package)
    return command.rstrip()

def parse_yaml_packages(filename):
    """Get a list of package names from yaml file"""
    packagesdict = {}
    with open(filename, 'r') as stream:
        packagesdict = yaml.load(stream)
    return packagesdict

def validate_config(config):
    for k, v in config.iteritems():
        assert type(k) is str
        assert type(v) is list
        assert len(v) is not 0
        for i in v:
            assert type(i) is str

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
    p.add_argument('-c', '--config', dest='configfile',
            help='yaml config file for jail/package mappings')
    p.add_argument('-d', '--dryrun', action='store_true',
            help='only print commands, do not run them')
    if not test_args == None:
        args = p.parse_args(test_args)
    else:
        args = p.parse_args()

    if (args.package is not None or args.jailpath is not None)\
            and args.configfile is not None:
        raise ArgumentError("--package and --jailpath args are mutually exclusive to --config\n")
    if args.configfile is None and not all([getattr(args,x) for x in ('package', 'jailpath')]):
        raise ArgumentError("--package and --jailpath arguments must be specified together (or use --config)\n")
    return args

def main():
    args = parse_args()

    # Not going to validate these - we'll be passing errors back from pkgng
    # anyway.
    package = args.package
    jailpath = args.jailpath
    dryrun = args.dryrun
    if args.configfile is not None:
        commands = yaml_to_commands(args.configfile) 
    else:
        commands = [generate_command(package, jailpath)]
    for command in commands: 
        if dryrun is True:
            print command
        else:
            run = Popen(string.split(command, ' '), stdin=PIPE, stderr=PIPE)
            status = run.wait()
            if run.stdout is not None:
                print "STDOUT:"
                for i in run.stdout.readlines(): print i
                run.stdout.close()
            if run.stderr is not None:
                print "STDERR:"
                for i in run.stderr.readlines(): print i
                run.stderr.close()
            if status != 0:
                print "Command '%s' did not complete successfully (code %d), exiting" % (command, status)
                sys.exit(status)
            else:
                print "Command '%s' successful" % command
