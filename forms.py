# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from contaku.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ['readed']

class SimpleContactForm(ContactForm):
    class Meta:
        model = Contact
        exclude = ['readed', 'name', 'organization','subject']