import pytest
import uniplot.analysis
import uniplot.parse

test_file = "resources/uniprot_sprot_small.xml.gz"

def test_average():
    assert uniplot.analysis.average_len(uniplot.parse.uniprot_seqrecords(test_file)) == 5449/18