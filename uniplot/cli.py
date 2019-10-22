from . import parse, analysis
import argparse
from . import plot


def dump():
    for x in parse.uniprot_seqrecords("./uniprot_receptor.xml.gz"):
        print(x)

def names():
    for x in parse.uniprot_seqrecords("./uniprot_receptor.xml.gz"):
        print(x.name)

def average():
    print("Average Length is {:.3f}".format(
        analysis.average_len(parse.uniprot_seqrecords("./uniprot_receptor.xml.gz"))))

def cli():
    #Create new parser
    parser = argparse.ArgumentParser(prog="uniplot")

    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(func=dump)
    subparsers.add_parser("list").set_defaults(func=names)
    subparsers.add_parser("average").set_defaults(func=average)
    subparsers.add_parser("plot-average-by-taxa").set_defaults(func=plot_average_by_taxa())

    #Parse the command line
    args = parser.parse_args()

    #Take the func argument
    args.func()

def plot_average_by_taxa():
    av = analysis.average_len_taxa(parse.uniprot_seqrecords("./uniprot_receptor.xml.gz"))
    plot.display_barplot(av)
