# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponseRedirect

from django.forms import ModelForm
#from django.utils.translation import ugettext_lazy as _


from contaku.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            c = form.save()            
        else:
            pass
    return HttpResponseRedirect(request.META['HTTP_REFERER'])