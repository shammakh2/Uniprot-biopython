import matplotlib.pyplot as mlot

def display_barplot (d, t_type):
    """Display a bar graph or pie chart, depending on given arguments, showing average sequence length per taxonomy"""
    recavg = [x[1] for x in list(d.values())]
    if t_type == 1:
        mlot.pie(recavg, labels=d.keys(), autopct='%.1f%%')
        mlot.show()
    else:
        r = range(0, len(d))
        mlot.figure()
        mlot.bar(r, recavg)
        mlot.xticks(r, d.keys())
        mlot.tight_layout()
        mlot.xticks(rotation=90)
        mlot.subplots_adjust(bottom=0.33)
        mlot.show()

def display_numpie (d):
    """Display a pie chart showing number of records in each taxanomic category at the given depth"""
    recnum = [x[0] for x in list(d.values())]
    jam = [x + '\n' + str(v[0]) for x, v in d.items()]
    mlot.pie(recnum, labels=jam)
    mlot.show()

