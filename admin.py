# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext as _

from contaku.models import Contact

USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)

class ContactAdmin(admin.ModelAdmin):
    pass

class SimpleContactAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'phone', 'email', 'readed']
    fields = ['date', 'name', 'phone', 'email', 'comment', 'readed']
    readonly_fields = ['date', 'name', 'phone', 'email', 'comment']
    list_filter = ['date', 'readed']

if USE_SIMPLE_CONTACT:
    admin.site.register(Contact, SimpleContactAdmin)
else:
    admin.site.register(Contact, ContactAdmin)