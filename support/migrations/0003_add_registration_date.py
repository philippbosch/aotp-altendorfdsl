# -*- coding: utf-8 -*-

from south.db import db
from django.db import models
from support.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'Supporter.date_registered'
        db.add_column('support_supporter', 'date_registered', models.DateTimeField(auto_now_add=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'Supporter.date_registered'
        db.delete_column('support_supporter', 'date_registered')
        
    
    
    models = {
        'support.supporter': {
            'date_registered': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
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
