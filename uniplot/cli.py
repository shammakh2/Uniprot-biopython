from . import parse, analysis, plot, deflocation
import argparse

def dump(location, args):
    """Print all records from generator"""
    for x in parse.uniprot_seqrecords(location):
        print(x)

def names(location, args):
    """Print all protein names from generator"""
    for x in parse.uniprot_seqrecords(location):
        print(x.name)

def average(location, args):
    """Print the average length of all proteins sequences in generator"""
    print("Average Length is {:.3f}".format(
        analysis.average_len(parse.uniprot_seqrecords(location))))

def plot_average_by_taxa(location, args):
    """Pass generator and depth for plotting averages"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(location), args.depth)
    plot.display_barplot(av, args.piemode)

def npie(location, args):
    """Pass generator and depth for plotting number of records"""
    av = analysis.average_len_taxa(parse.uniprot_seqrecords(location), args.depth)
    plot.display_numpie(av)

def loco(gems):
    """Save entered file location"""
    deflocation.locorec(gems.location)


def loc(args, loco = None):
    """Pass temporary or saved location and run functions. Priority given to temporary location"""
    location = deflocation.locoload()
    if loco != None:
        args.func(loco, args)
    else:
        args.func(location, args)


def cli():
    """Parse all arguments from commandline and call appropriate functions"""
    #Create new parser
    parser = argparse.ArgumentParser(description="This program analyses and returns GNU zipped uniprot-xml database files")
    parser.add_argument("--loco", type=str, default=None, help="Use '--loco' to pass in a temporary file location", metavar='file-location')
    #Add subparsers
    subparsers = parser.add_subparsers(help="Sub Command Help")

    f_location = subparsers.add_parser('location', help="Use 'location' to save the file location that you want to run other commands on")
    f_location.add_argument('location', type=str,metavar='file_location', help='Type your file location in place of "file location"')
    f_location.set_defaults(func=loco)
    subparsers.add_parser("dump", help="Use 'dump' to print all the records from the file").set_defaults(run=loc, func=dump)
    subparsers.add_parser("list", help="Use 'list' to print all the protein sequence names from the file").set_defaults(run=loc, func=names)
    subparsers.add_parser("average", help="Use 'average' to obtain the average length of proteins from all records of the file").set_defaults(run=loc, func=average)
    taxanom = subparsers.add_parser("plot-taxa", help='Plot the average lengths of proteins distributed by all categories at a taxonomy level as a bar graph or pie chart. Use help argument(-h) with plot-taxa for more detail')
    taxanom.add_argument("--depth", type=int, default=0,metavar="<Level number>", help='Use this optional argument to supply the level of taxonomy you want to access (1 is the highest and is the default value)')
    taxanom.add_argument("--piemode", type=int, default=0,metavar=" [1 or 0] ", help='If you want to see the average graph in the form of a pie chart, pass the value 1 with this argument(1 = True and default is false)')
    taxanom.set_defaults(run=loc, func=plot_average_by_taxa)
    numpie = subparsers.add_parser("pie", help="Give the number of records sorted by taxanomic categories in the form of a pie chart.(depth argument can be passed to change taxanomy level. Use '-h' with pie for more information")
    numpie.add_argument("--depth", type=int, default=0, help='Use this optional argument to supply the level of taxonomy you want to access (1 is the highest and is the default value)')
    numpie.set_defaults(run=loc, func=npie)

    #Parse the command line
    args = parser.parse_args()
    args.run(args, args.loco)


