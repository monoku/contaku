# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

class Contact(models.Model):
    """ You need to subclass this in order to change the contact form.
    """
    date = models.DateTimeField(auto_now=True, verbose_name= _(u'Date & Time'))
    #name = models.CharField(max_length=200, verbose_name= _(u'Name'), null=True)
    #email = models.EmailField(verbose_name= _('Email'))
    #phone = models.CharField(max_length=200, verbose_name=_(u'Phone'), null=True)
    #organization = models.CharField(max_length=200, verbose_name=_(u'Organization/Company'), null=True)

    #subject = models.CharField(max_length=30, verbose_name=_(u'Subject'), null=True)
    comment = models.TextField(verbose_name= _(u'Message'))
    
    readed = models.BooleanField(default=False, verbose_name = _(u'Readed?'))
    date_read = models.DateTimeField(blank=True, null=True, verbose_name= _(u'Date & time readed'))

    def get_absolute_url(self):
        return reverse('admin:contact_contact_change', args=[self.id])

    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')
