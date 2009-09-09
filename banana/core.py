#!/usr/bin/python
import re
import sys
import os
import logging
import logger
import glob
from registration import matchingDict
from exceptions import MultipleMatchException, NoMatchException
from utils import normalize, locate

log = logging.getLogger('banana')
files = set()


class TestInstance(object):
    pass


def test_scenario(scenarioLines, testInstance):
    #TODO: account for parameterised tests
    line_iter = iter(scenarioLines)
    for line in line_iter:
        line = line.strip()
        matched = False
        try:
            for regex, func in matchingDict.iteritems():
                match = re.search(regex, line)
                if match is not None:
                    if matched:
                        raise MultipleMatchException('A sentence was matched twice')
                    matched = True
                    func(testInstance, *match.groups())
            if not matched:
                raise NoMatchException('No matching function for line: ' + line)
        except Exception as inst:
            log.warning(line)
            log.error('#FAILED: '+ str(type(inst)) + str(inst.args))
            for line in line_iter: #display all remaining lines
                log.info(line)
            raise
        else:
            log.success(line)


def register_module(module, testClass):
    """Register a python module and prepare a testClass with all 
    contained scenario files.
    """
    path = os.path.dirname(module.__file__)
    for f in locate('*.scenario', path):
        files.add(f)
    __import__(module.__name__+".rules")
    
    for f in files:
        def _wrap(self, f=f):
            def _inner(f):
                return run_test(f, self)
            return _inner(f)
        
        setattr(
            testClass,
            'test_'+ normalize(f, path), 
            _wrap)


def run_test(f, testInstance=TestInstance()):
    print '' #starting with a newline so we don't look ugly
    return test_scenario(
        [line.rstrip() for line in open(f).readlines()],
        testInstance)
