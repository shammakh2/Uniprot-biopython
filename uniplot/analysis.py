def average_len(records):
    """"Return average length for record."""
    count = 0
    record_num = 0
    for x in records:
        count = count + len(x)
        record_num = record_num + 1
    return count/record_num

def average_len_taxa(records, depth):
    record_by_taxa = {}
    depth = int(depth)
    if depth <= 0:
        depth = 0
    elif depth >= 0:
        depth = depth - 1
    for r in records:
        taxa = r.annotations["taxonomy"][depth]
        record_by_taxa.setdefault(taxa, 1)
        if taxa in record_by_taxa:
            record_by_taxa[taxa] = record_by_taxa[taxa]+1
    return record_by_taxa
