
def locorec(var):
    """Truncate file and write inputted location"""
    f = open('./uniplot/location', 'w')
    f.write(var)
    f.close()

def locoload():
    """Read location from file"""
    f = open('./uniplot/location', 'r')
    location = f.read()
    return location.strip()
