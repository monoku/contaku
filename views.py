# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect

USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)

if USE_SIMPLE_CONTACT:
    from contaku.forms import SimpleContactForm as ContactForm
else:
    from contaku.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            c = form.save()            
        else:
            pass
    return HttpResponseRedirect(request.META['HTTP_REFERER'])