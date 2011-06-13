# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
        
CONTACT_FORM = getattr(settings, 'CONTACT_FORM', None)
CONTACT_MODEL = getattr(settings, 'CONTACT_MODEL', None)


if CONTACT_FORM:
    # if the user defined a contact form i shall use it:
    pass
    # TODO import this form as ContactForm
elif CONTACT_MODEL:
    # if the user defined a contact model i shall use it:
    class ContactForm(ModelForm):
        class Meta:
            model = CONTACT_MODEL
            exclude = ['readed','date_read']
else:
    # use our default contact form
    from contaku.models import Contact

    class ContactForm(ModelForm):
        class Meta:
            model = Contact
            exclude = ['readed','date_read']