from django.test import TestCase
from banana import register_module
import scenarios
import os

class BananaTest(TestCase):
    pass

register_module(scenarios, BananaTest)