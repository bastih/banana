matchingDict = {}

def matches(regex):
    def decorated(f):
        matchingDict[regex] = f
        return f
    return decorated
