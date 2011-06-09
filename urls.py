# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from monoku.contact.views import contact

urlpatterns = patterns('',
    url(r'^$', contact, name='contact-action'),
)