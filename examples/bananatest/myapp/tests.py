from django.test import TestCase
from banana import register_module, register_class, matches
import scenarios
import os

class BananaTest(TestCase):
    pass

class InlineTest(TestCase):
    """An alternative way to represent tests"""
    @matches(r'^Given the user opens some weird page')
    def inclassInit(self):
        self.response = self.client.get('/admin/')
    
    def scenario_cool(self):
        """Given the user opens some weird page
        The page should contain the text "Username"
        The page should contain the text "Password"
        """
    
    
register_class(InlineTest)
register_module(scenarios, BananaTest)
#register_class(scenarios.rules, InlineTest)