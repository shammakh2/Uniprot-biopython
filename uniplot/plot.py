import matplotlib.pyplot as mlot

def display_barplot (d):
    r = range(0,len(d))
    # mlot.figure()
    #
    # mlot.bar(r, d.values())
    # mlot.xticks(r, d.keys())
    # mlot.tight_layout()
    # mlot.xticks(rotation=90)
    # mlot.subplots_adjust(bottom=0.33)
    # mlot.show()
    mlot.pie(d.values(), labels=d.keys())
    mlot.show()
    print(d)