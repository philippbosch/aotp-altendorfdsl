
from south.db import db
from django.db import models
from support.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Supporter'
        db.create_table('support_supporter', (
            ('id', models.AutoField(primary_key=True)),
            ('vorname', models.CharField(max_length=100)),
            ('nachname', models.CharField(max_length=100)),
            ('strasse', models.CharField(max_length=250)),
            ('plz', models.IntegerField()),
            ('ort', models.CharField(max_length=100)),
            ('email', models.EmailField()),
            ('verified', models.CharField(max_length=1)),
        ))
        db.send_create_signal('support', ['Supporter'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Supporter'
        db.delete_table('support_supporter')
        
    
    
    models = {
        'support.supporter': {
            'email': ('models.EmailField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'nachname': ('models.CharField', [], {'max_length': '100'}),
            'ort': ('models.CharField', [], {'max_length': '100'}),
            'plz': ('models.IntegerField', [], {}),
            'strasse': ('models.CharField', [], {'max_length': '250'}),
            'verified': ('models.CharField', [], {'max_length': '1'}),
            'vorname': ('models.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['support']
