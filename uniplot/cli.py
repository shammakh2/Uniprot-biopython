import gzip
from Bio import SeqIO
import argparse

def dump():
    handle = gzip.open("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz")
    for x in SeqIO.parse(handle,"uniprot-xml"):
        print(x)

def names():
    handle = gzip.open("H:/CSC1034/Practical-2/uniprot_receptor.xml.gz")
    for x in SeqIO.parse(handle, "uniprot-xml"):
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

