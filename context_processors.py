# -*- coding: utf-8 -*-

from django.conf import settings

from django.forms import ModelForm
#from django.utils.translation import ugettext_lazy as _


from contaku.forms import ContactForm

def contact(request):
    data = {}
    data['contact_form'] = ContactForm()
    data['contact_action'] = 'contact-action'
    return data