import os
import fnmatch

def normalize(filename, rel_to='.'):
    relativePath = os.path.relpath(filename, start=rel_to)
    normalizedFileName = "_".join(os.path.split(relativePath))
    normalizedFileName = normalizedFileName.replace('.', '_')
    return normalizedFileName

"""Locate from http://code.activestate.com/recipes/499305/"""

def locate(pattern, root=os.curdir):
    """Locate all files matching supplied filename pattern in and below
    supplied root directory"""
    for path, dirs, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(path, filename)