from . import parse
import argparse


def dump():
    for x in parse.uniprot_seqrecords("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz"):
        print(x)

def names():
    for x in parse.uniprot_seqrecords("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz"):
        print(x.name)

def cli():
    #Create new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)

    #Parse the command line
    args = parser.parse_args()

    #Take the func argument
    args.func()

