from . import parse
from . import analysis
import argparse


def dump():
    for x in parse.uniprot_seqrecords("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz"):
        print(x)

def names():
    for x in parse.uniprot_seqrecords("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz"):
        print(x.name)

def average():
    print("Average Length is {}".format(
        analysis.average_len(parse.uniprot_seqrecords("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz"))))

def cli():
    #Create new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)

    #Parse the command line
    args = parser.parse_args()

    #Take the func argument
    args.func()

