#!/usr/bin/python
import re
import sys
import os
import logging
import logger
import glob
import types
from registration import matchingDict
from exceptions import MultipleMatchException, NoMatchException
from utils import normalize, locate
 
log = logging.getLogger('banana')


class TestInstance(object):
    """Provide an empty object as common ground between tests"""
    pass

def test_scenario(scenarioLines, testInstance):
    """
    Parse scenario lines and run matching function
    """
    #TODO: account for parameterised tests
    line_iter = iter(scenarioLines)
    for line in line_iter:
        line = line.strip()
        if not len(line):
            continue
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

def create_test_wrap(f):
    def _wrap(self, f=f):
        def _inner(f):
            return run_test(f, self)
        return _inner(f)
    return _wrap


def register_module(module, testClass):
    """
    Register a python module and prepare a testClass with all 
    contained scenario files.
    """
    path = os.path.dirname(module.__file__)
    __import__(module.__name__+".rules")
    for f in locate('*.scenario', path):
        setattr(
            testClass,
            'test_'+ normalize(f, path), 
            create_test_wrap(open(f).xreadlines())
        )

def register_class(testClass):
    """
    Register a class with scenario-docstrings for testing
    """
    for name in dir(testClass):
        func = getattr(testClass, name)
        if name.startswith('scenario') and type(func) is types.FunctionType:
            setattr(
                testClass,
                'test'+name[7:],
                create_test_wrap(func.__doc__.split('\n'))
            )
            
def run_test(lines, testInstance=TestInstance()):
    print '' #starting with a newline so we don't look ugly
    return test_scenario(lines, testInstance)
