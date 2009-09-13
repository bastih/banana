from django.test import Client
from banana.registration import matches

@matches(r'^Given the user opens the page$')
def adminInit(t):
    t.response = t.client.get('/myapp/testview')

@matches(r'^Given the user opens the admin$')
def adminInit(t):
    t.response = t.client.get('/admin/')
    
@matches(r'^The page should contain the text "(.*)"$')
def pageContains(t, text):
    assert(t.response is not None)
    t.assertContains(t.response, text)