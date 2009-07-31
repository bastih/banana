import re
from registration import matchingDict

class TestInstance(object):
    pass

import rules

testInstance = TestInstance()
for line in open('scenario.feature'):
    matched = False
    print line.strip()
    for regex, func in matchingDict.iteritems():
        match = re.search(regex,line)
        if match is not None:
            if matched:
                raise Exception, 'A sentence was matched twice'
            matched = True
            try:
                func(testInstance, *match.groups())
            except Exception:
                print 'Failed because of Exception'
        
    if not matched:
        raise Exception, 'No matching function for the line:' + line