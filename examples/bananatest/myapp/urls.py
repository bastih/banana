from django.conf.urls.defaults import *
from views import testView

urlpatterns = patterns('',
    # Example:
    url(r'^testview$', testView),
    
)