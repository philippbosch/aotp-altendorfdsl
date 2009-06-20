# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.template import Template, Context
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings

from htmlentitydefs import name2codepoint as n2cp
import re
import hashlib

from content.models import Text
from support.models import Supporter
import support.forms

def show_page(request, slug, template='default.html', form=None):
    text = get_object_or_404(Text, slug=slug)
    if form:
        form = getattr(support.forms, form)
        if request.method == 'POST':
            form_instance = form(request.POST)
            if form_instance.is_valid():
                supporter = form_instance.save()
                
                # send email
                mailtext = get_object_or_404(Text, slug='confirm-email')
                t = Template(mailtext.text)
                c = Context({'confirm_link': 'http://%(hostname)s%(url)s' % {'hostname': request.META['HTTP_HOST'], 'url': reverse('support_confirm', kwargs={'id': supporter.id, 'hash': hashlib.sha224(str(supporter.id) + settings.SECRET_KEY).hexdigest()})}, 'request': request})
                html = t.render(c)
                msg = EmailMultiAlternatives(mailtext.title, decode_htmlentities(strip_tags(html)), 'info@dsl-altendort-ersdorf.de', [supporter.email])
                msg.attach_alternative(html, "text/html")
                msg.send()
                return HttpResponseRedirect(reverse('show_page', kwargs={'slug':'danke'}))
        else:
            form_instance = form()
    else:
        form_instance = None
    return render_to_response(template, { 'text': text, 'form': form_instance }, context_instance=RequestContext(request))


def confirm(request, id, hash):
    supporter = get_object_or_404(Supporter, id=id)
    supporter.verified = True
    supporter.save()
    return HttpResponseRedirect(reverse('show_page', kwargs={'slug':'confirmed'}))


def html2text(value):
    """
    Pipes given HTML string into the text browser W3M, which renders it.
    Rendered text is grabbed from STDOUT and returned.
    """
    try:
        cmd = "w3m -dump -T text/html -O ascii"
        proc = Popen(cmd, shell = True, stdin = PIPE, stdout = PIPE)
        return proc.communicate(str(value))[0]
    except OSError:
        # something bad happened, so just return the input
        return value



def substitute_entity(match):
    ent = match.group(2)
    if match.group(1) == "#":
        return unichr(int(ent))
    else:
        cp = n2cp.get(ent)

        if cp:
            return unichr(cp)
        else:
            return match.group()

def decode_htmlentities(string):
    entity_re = re.compile("&(#?)(\d{1,5}|\w{1,8});")
    return entity_re.subn(substitute_entity, string)[0]
