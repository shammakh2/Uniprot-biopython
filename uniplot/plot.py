import matplotlib.pyplot as mlot

def display_barplot (d, t_type):
    recnum = [x[0] for x in list(d.values())]
    jam = {x + '\n' + str(v[0]) for x, v in d.items()}
    if t_type == 1:
        mlot.pie(recnum, labels=jam, autopct='%.1f%%')
        mlot.show()
    else:
        r = range(0, len(d))
        mlot.figure()
        recavg = [x[1] for x in list(d.values())]
        mlot.bar(r, recavg)
        mlot.xticks(r, d.keys())
        mlot.tight_layout()
        mlot.xticks(rotation=90)
        mlot.subplots_adjust(bottom=0.33)
        mlot.show()
