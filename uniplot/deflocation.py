
def locorec(var):
    f = open('./uniplot/location', 'w')
    f.write(var)
    f.close()

def locoload():
    f = open('./uniplot/location', 'r')
    location = f.read()
    return location.strip()
