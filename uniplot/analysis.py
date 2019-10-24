def average_len(records):
    """"Return average length for record."""
    count = 0
    for x in records:
        count = count + len(x)
    return count/len(records)

def average_len_taxa(records, depth):
    record_by_taxa = {}
    depth = int(depth)
    if depth <= 0:
        depth = 0
    elif depth >= 0:
        depth = depth - 1
    for r in records:
        taxa = r.annotations["taxonomy"][depth]
        record_by_taxa.setdefault(taxa, []).append(r)
    return {taxa:average_len(record) for (taxa, record) in record_by_taxa.items()}