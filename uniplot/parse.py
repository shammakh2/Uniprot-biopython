import gzip
from Bio import SeqIO
import io

def uniprot_seqrecords(file_location):
    """Open GNU uniprot xml zipped file type and return it as a generator"""
    handle = gzip.open(file_location)
    buff = io.BufferedReader(handle,200000000)
    return SeqIO.parse(buff, "uniprot-xml")

