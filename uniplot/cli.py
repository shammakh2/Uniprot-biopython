from . import parse, analysis
import argparse
from . import plot
import time

def dump(loco):
    for x in parse.uniprot_seqrecords(loco):
        print(x)

def names(loco):
    for x in parse.uniprot_seqrecords(loco):
        print(x.name)
def average(loco):
    print("Average Length is {:.3f}".format(
        analysis.average_len(parse.uniprot_seqrecords(loco))))

def loc(loco, args, depth = None, pie = None):
    if depth != None:
        args(depth, loco, pie)
    else:
        args(loco)

def cli():
    #Create new parser
    parser = argparse.ArgumentParser(prog="uniplot")
    parser.add_argument("--loco", type=str, default="./resources/uniprot_sprot_small.xml.gz")
    parser.set_defaults(func=loc)
    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("dump").set_defaults(run=loc, func=dump)
    subparsers.add_parser("list").set_defaults(run=loc, func=names)
    subparsers.add_parser("average").set_defaults(run=loc, func=average)
    taxanom = subparsers.add_parser("plot-average-by-taxa")
    taxanom.add_argument("--depth", type=int, default=0)
    taxanom.add_argument("--pie", type=int, default=0)
    taxanom.set_defaults(run=loc, func=plot_average_by_taxa)

    #Parse the command line
    args = parser.parse_args()
    #Take the func argument
    if hasattr(args,'depth'):
        args.run(args.loco, args.func, args.depth, args.pie)
    else:
        args.run(args.loco, args.func)


def plot_average_by_taxa(depth, loco, pie):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(loco), depth)
    plot.display_barplot(av, pie)

