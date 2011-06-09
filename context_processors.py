# -*- coding: utf-8 -*-

from django.conf import settings

from contaku.forms import ContactForm, SimpleContactForm

USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)

def contact(request):
    data = {}
    if USE_SIMPLE_CONTACT:
        contact_form = SimpleContactForm()
    else:
        contact_form = ContactForm()
    data['contact_form'] = contact_form
    data['contact_action'] = 'contact-action'
    return data