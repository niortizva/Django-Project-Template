from django.conf.urls import url
from web.views import test

urlpatterns = [
    url(r'', test, name="test"),
]
