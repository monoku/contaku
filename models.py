# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
from django.template.loader import render_to_string
from django.template import Context

EMAIL_SUBJECT_PREFIX = getattr(settings, 'EMAIL_SUBJECT_PREFIX', '')
EMAIL_HOST_USER = getattr(settings, 'EMAIL_HOST_USER', '')
ADMINS = getattr(settings, 'ADMINS', ())
MANAGERS = getattr(settings, 'MANAGERS', ())
TO = getattr(settings, 'CONTACT_TO', '')
BCC = getattr(settings, 'CONTACT_BCC', ())
SEND_TO_ADMINS = getattr(settings, 'SEND_TO_ADMINS', True)
SEND_TO_MANAGERS = getattr(settings, 'SEND_TO_MANAGERS', True)
REPLY_TO_SENDER = getattr(settings, 'REPLY_TO_SENDER', True)
USE_SIMPLE_CONTACT = getattr(settings, 'USE_SIMPLE_CONTACT', True)
CONTACT_COLOR_ONE = getattr(settings, 'CONTACT_COLOR_ONE', '#000000')
CONTACT_COLOR_TWO = getattr(settings, 'CONTACT_COLOR_TWO', '#777777')
STATIC_URL = getattr(settings, 'STATIC_URL', '')

class Contact(models.Model):
    date = models.DateTimeField(auto_now=True, verbose_name= _(u'Date & Time'))
    name = models.CharField(max_length=200, verbose_name= _(u'Name'), null=True)
    email = models.EmailField(verbose_name= _('Email'))
    phone = models.CharField(max_length=200, verbose_name=_(u'Phone'), null=True)
    organization = models.CharField(max_length=200, verbose_name=_(u'Organization/Company'), null=True)
    subject = models.CharField(max_length=30, verbose_name=_(u'Subject'), null=True)
    comment = models.TextField(verbose_name= _(u'Message'))
    readed = models.BooleanField(default=False, verbose_name = _(u'Readed?'))

    def get_absolute_url(self):
        return reverse('admin:contaku_contact_change', args=[self.id])

    class Meta:
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')

def send_contact_email(sender, instance, created, **kwargs):
    subject = '%s %s ' % (EMAIL_SUBJECT_PREFIX, instance.subject)
    subject = ''.join(subject.splitlines())
    from_email = EMAIL_HOST_USER
    bcc = []
    if BCC:
        bcc += BCC
    if SEND_TO_ADMINS:
        bcc += [admin[1] for admin in ADMINS]
    if SEND_TO_MANAGERS:
        bcc += [manager[1] for manager in MANAGERS]
    # Rendering Templates
    context = {}
    context['message'] = instance
    context['site'] = Site.objects.get_current()
    context['color_one'] = CONTACT_COLOR_ONE
    context['color_two'] = CONTACT_COLOR_TWO
    context['STATIC_URL'] = STATIC_URL
    
    if USE_SIMPLE_CONTACT:
        text_content = render_to_string('contact/content_simple.txt', Context(context))
        html_content = render_to_string('contact/content_simple.html', Context(context))
    else:
        text_content = render_to_string('contact/content.txt', Context(context))
        html_content = render_to_string('contact/content.html', Context(context))
    # Formating email data
    email_data = {}
    email_data['subject'] = subject
    email_data['body'] = text_content
    email_data['from_email'] = from_email
    email_data['to'] = [TO]
    email_data['bcc'] = bcc
    if REPLY_TO_SENDER:
        email_data['headers'] = {'Reply-To': instance.email}
    msg = EmailMultiAlternatives(**email_data)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

post_save.connect(send_contact_email, sender=Contact)