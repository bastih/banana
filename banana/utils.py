import os

def normalize(filename, rel_to='.'):
    normalizedFileName = "_".join(os.path.split(os.path.relpath(filename, start=rel_to)))
    normalizedFileName = normalizedFileName.replace('.','_')
    return normalizedFileName