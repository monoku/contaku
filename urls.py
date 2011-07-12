# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from contaku.views import contact

urlpatterns = patterns('',
    url(r'^$', contact, name='contact-action'),
)