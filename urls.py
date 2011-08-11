# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from contaku.views import contact, contact_json

urlpatterns = patterns('',
    url(r'^$', contact, name='contact-action'),
    url(r'^json/$', contact, name='contact-action-json'),
)