import gzip
from Bio import SeqIO
import io

def uniprot_seqrecords(file_location):
    handle = gzip.open(file_location)
    test = io.BufferedReader(handle,200000000)
    return SeqIO.parse(test, "uniprot-xml")

