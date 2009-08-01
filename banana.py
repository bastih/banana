#!/usr/bin/python
import re
import sys
import glob
import os
import curses
import logger
import logging
from registration import matchingDict


log = logging.getLogger('banana')


class TestInstance(object):
    pass

def testScenario(scenarioLines):
    testInstance = TestInstance()
    broken = False
    for line in scenarioLines:
        matched = False
        if broken:
            break
        try:
            for regex, func in matchingDict.iteritems():
                match = re.search(regex, line)
                if match is not None:
                    if matched:
                        raise Exception, 'A sentence was matched twice'
                    matched = True
                    func(testInstance, *match.groups())
            if not matched:
                raise Exception, 'No matching function for the line:' + line
        except Exception, detail:
            log.warning(line.strip())
            log.error('#FAILED: '+ str(detail))
            broken = True
        else:
            log.success(line.strip())
        
    return not broken

def main():
    path = sys.argv[1]
    importedruleset =  __import__(path+'.rules')
    results = {'failed':0,'success':0}
    for f in glob.glob(path+'/*.feature'):
        log.info(f+':')
        result = testScenario([line.rstrip() for line in open(f).readlines()])
        results['success' if result else 'failed'] += 1
    log.info(str(results))
        
if __name__ == '__main__':
    main()