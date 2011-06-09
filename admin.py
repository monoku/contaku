# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext as _

from contaku.models import Contact

USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)

class ContactAdmin(admin.ModelAdmin):
    pass

class SimpleContactAdmin(adminModelAdmin):
    pass

if USE_SIMPLE_CONTACT:
    admin.site.register(Contact, SimpleContactAdmin)
else:
    admin.site.register(Contact, ContactAdmin)