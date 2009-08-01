from banana.rules import matches

@matches(r'/Given I open (http://.*)')
def openWebpage(t, url):
    print url