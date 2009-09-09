# Create your views here.

from django.http import HttpResponse

def testView(request):
    return HttpResponse('I am a text in a view')
    