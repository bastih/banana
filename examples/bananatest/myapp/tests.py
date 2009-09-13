from django.test import TestCase
from banana import register_module, register_class
import scenarios
import os

class BananaTest(TestCase):
    pass

class InlineTest(TestCase):
    
    def scenario_cool(self):
        """Given the user opens the admin
        The page should contain the text "Username"
        The page should contain the text "Password"
        """
        pass
    
    

register_module(scenarios, BananaTest)
register_class(scenarios.rules, InlineTest)