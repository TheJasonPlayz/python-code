def intSplit(int):
    intStr = str(int)
    return [char for char in intStr]

def listJoin(list):
    string = ''
    first = True
    for char in list:
        if first:
            string += char
            first = False
        else:
            string += "+" + char
    return string