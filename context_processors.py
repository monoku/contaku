# -*- coding: utf-8 -*-

from django.conf import settings

from contaku.forms import ContactForm, SimpleContactForm

USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)

def contact(request):
    if USE_SIMPLE_CONTACT:
        contact_form = SimpleContactForm()
    else:
        contact_form = ContactForm()
    return {'contact_form':contact_form}