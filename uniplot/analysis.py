def average_len(records):
    """"Return average length for record."""
    count = 0
    for x in records:
        count = count + len(x)
    return count/len(records)
