# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from support.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Changing field 'Supporter.verified'
        db.alter_column('support_supporter', 'verified', models.BooleanField())
        
    
    
    def backwards(self, orm):
        
        # Changing field 'Supporter.verified'
        db.alter_column('support_supporter', 'verified', models.CharField(max_length=1))
        
    
    
    models = {
        'support.supporter': {
            'email': ('models.EmailField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'nachname': ('models.CharField', [], {'max_length': '100'}),
            'ort': ('models.CharField', [], {'max_length': '100'}),
            'plz': ('models.IntegerField', [], {}),
            'strasse': ('models.CharField', [], {'max_length': '250'}),
            'verified': ('models.BooleanField', [], {}),
            'vorname': ('models.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['support']
