# -*- coding: utf-8 -*-
from django.db import models

class Supporter(models.Model):
    vorname = models.CharField(max_length=100, verbose_name="Vorname")
    nachname = models.CharField(max_length=100, verbose_name="Nachname")
    strasse = models.CharField(max_length=250, verbose_name="Straße")
    plz = models.IntegerField(verbose_name="PLZ")
    ort = models.CharField(max_length=100, verbose_name="Ort")
    email = models.EmailField(verbose_name="E-Mail")
    verified = models.BooleanField(verbose_name="Bestätigt?")
    date_registered = models.DateTimeField(auto_now_add=True, verbose_name="Registrierungsdatum")
    
    def __unicode__(self):
        return '%s %s' % (self.vorname, self.nachname)
    
    class Meta:
        verbose_name = "Unterstützer"
        verbose_name_plural = "Unterstützer"