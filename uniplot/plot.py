import matplotlib.pyplot as mlot

def display_barplot (d, t_type):
    print(d)
    print(d.values)
    recavg = [x[1] for x in list(d.values())]
    print(recavg)
    jam = [x + '\n' + str(v[0]) for x, v in d.items()]
    if t_type == 1:
        mlot.pie(recavg, labels=jam, autopct='%.1f%%')
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
    print(d)
    print(d.values)
    recnum = [x[0] for x in list(d.values())]
    print(recnum)
    jam = [x + '\n' + str(v[0]) for x, v in d.items()]
    mlot.pie(recnum, labels=jam, autopct='%.1f%%')
    mlot.show()

