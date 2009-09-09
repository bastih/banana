#!/usr/bin/python
import re, sys, glob, os, logging
import logger
from registration import matchingDict
from utils import normalize

log = logging.getLogger('banana')

files = set()

class TestInstance(object):
    pass

def testScenario(scenarioLines, testInstance):
    #TODO: account for parameterised tests
    broken = False
    lineIt = iter(scenarioLines)
    for line in lineIt:
        matched = False
        try:
            for regex, func in matchingDict.iteritems():
                match = re.search(regex, line)
                if match is not None:
                    if matched:
                        raise Exception, 'A sentence was matched twice'
                    matched = True
                    func(testInstance, *match.groups())
            if not matched:
                raise Exception, 'No matching function for line: ' + line
        except Exception, detail:
            log.warning(line.strip())
            log.error('#FAILED: '+ str(type(detail)) + str(detail))
            for line in lineIt:
                log.info(line.strip()+' # ignored')
            raise
        else:
            log.success(line.strip())
    return not broken

def registerScenarioModule(module, testClass):
    path = os.path.dirname(module.__file__)
    featurepath = os.path.join(path,'*.scenario')
    for f in glob.glob(featurepath):
        files.add(f)
    __import__(module.__name__+".rules")

    for f in files:
        def _wrap(self, f = f):
            def _inner(f):
                return runTest(f, self)
            return _inner(f)
        setattr(testClass, 'test_'+ normalize(f, os.path.dirname(module.__file__)), _wrap)

def runTest(f, testInstance=TestInstance()):
    print '' #starting with a newline so we don't look ugly
    return testScenario([line.rstrip() for line in open(f).readlines()], testInstance)

def runTests(testInstance=TestInstance()):
    results = {'failed':0,'success':0}
    for f in files:
        log.info(f+':')
        result = runTest(f, testInstance)
        results['success' if result else 'failed'] += 1