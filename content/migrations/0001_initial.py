
from south.db import db
from django.db import models
from content.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Text'
        db.create_table('content_text', (
            ('id', models.AutoField(primary_key=True)),
            ('title', models.CharField(max_length=255)),
            ('text', models.TextField()),
            ('slug', models.SlugField()),
        ))
        db.send_create_signal('content', ['Text'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Text'
        db.delete_table('content_text')
        
    
    
    models = {
        'content.text': {
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'slug': ('models.SlugField', [], {}),
            'text': ('models.TextField', [], {}),
            'title': ('models.CharField', [], {'max_length': '255'})
        }
    }
    
    complete_apps = ['content']
