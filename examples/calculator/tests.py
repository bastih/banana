#!/usr/bin/env python

from unittest import TestCase, TextTestRunner, defaultTestLoader as loader
from banana import register_module 
import scenarios

class CalculatorTestCase(TestCase):
    pass

register_module(scenarios, CalculatorTestCase)

if __name__ == '__main__':
    suite = loader.loadTestsFromTestCase(CalculatorTestCase)
    print dir(CalculatorTestCase)
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)