from django.test import TestCase
from banana import registerScenarioModule
import scenarios
import os

class BananaTest(TestCase):
    pass

registerScenarioModule(scenarios, BananaTest)