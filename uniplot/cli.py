from . import parse, analysis, plot, deflocation
import argparse

def dump(location, args):
    for x in parse.uniprot_seqrecords(location):
        print(x)

def names(location, args):
    for x in parse.uniprot_seqrecords(location):
        print(x.name)

def average(location, args):
    print("Average Length is {:.3f}".format(
        analysis.average_len(parse.uniprot_seqrecords(location))))

def plot_average_by_taxa(location, args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(location), args.depth)
    plot.display_barplot(av, args.pie)

def numpie(location, args):
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(location), args.depth)
    plot.display_barplot(av, args.pie)

def loco(gems):
    deflocation.locorec(gems.location)


def loc(args, loco = None):
    location = deflocation.locoload()
    if loco != None:
        args.func(loco, args)
    else:
        args.func(location, args)


def cli():
    #Create new parser
    parser = argparse.ArgumentParser(prog="uniplot")
    parser.add_argument("--loco", type=str, default=None)
    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    f_location = subparsers.add_parser('location')
    f_location.add_argument('location', type=str)
    f_location.set_defaults(func=loco)
    subparsers.add_parser("dump").set_defaults(run=loc, func=dump)
    subparsers.add_parser("list").set_defaults(run=loc, func=names)
    subparsers.add_parser("average").set_defaults(run=loc, func=average)
    taxanom = subparsers.add_parser("plot-taxa")
    taxanom.add_argument("--depth", type=int, default=0)
    taxanom.add_argument("--pie", type=int, default=0)
    taxanom.set_defaults(run=loc, func=plot_average_by_taxa)
    numpie = subparsers.add_parser("pie")
    numpie.add_argument("--depth", type=int, default=0)
    numpie.set_defaults(run=loc, func=numpie)

    #Parse the command line
    args = parser.parse_args()
    args.run(args, args.loco)


