import matplotlib.pyplot as mlot

def display_barplot (d, t_type):
    jam = {x+'\n'+str(v) for x, v in d.items()}
    if t_type == 1:
        mlot.pie(d.values(), labels=jam, autopct='%.1f%%')
        mlot.show()
    else:
        r = range(0, len(d))
        mlot.figure()

        mlot.bar(r, d.values())
        mlot.xticks(r, d.keys())
        mlot.tight_layout()
        mlot.xticks(rotation=90)
        mlot.subplots_adjust(bottom=0.33)
        mlot.show()
