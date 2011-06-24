# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect

USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)

if USE_SIMPLE_CONTACT:
    from contaku.forms import SimpleContactForm as ContactForm
else:
    from contaku.forms import ContactForm

def contact(request):
    #TODO: implement strategy pattern
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("The message of contact was send succesfull"))
        else:
            for key, value in form.errors.iteritems():
                label = form.fields[key].label
                messages.warning(request, '%s: %s' % (label, ''.join([v for v in value])))
    return HttpResponseRedirect(request.META['HTTP_REFERER'])