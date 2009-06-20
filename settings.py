_ = lambda s:s

import os.path

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_NAME = os.path.split(PROJECT_ROOT)[-1]

#
# DEBUGGING
#

DEBUG = False
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ()

#
# CACHE
#

CACHE_BACKEND = 'locmem://'
CACHE_MIDDLEWARE_KEY_PREFIX = '%s_' % PROJECT_NAME
CACHE_MIDDLEWARE_SECONDS = 600

#
# EMAIL / ERROR NOTIFY
#

SERVER_EMAIL = 'pb@philippbosch.de'

ADMINS = (
    ('Philipp Bosch', 'philipp.bosch@me.com'),
)

MANAGERS = ADMINS

#
# DATABASE
# 

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = PROJECT_NAME
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

# DATABASE_ENGINE = 'sqlite3'
# DATABASE_NAME = './db.sqlite'


#
# I18N
#

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de'
LANGUAGES = (
    ('de', 'Deutsch'),
    # ('en', 'English'),
)
USE_I18N = True



#
# URLS
#

SITE_ID = 1

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

# PREPEND_WWW = True


#
# APPLICATION / MIDDLEWARE
#

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.markup',
    
    'south',
    'tinymce',
    'filebrowser',
    'sorl.thumbnail',
    
    'content',
    'support',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
)

#
# SECRET
#

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)



# Override the server-derived value of SCRIPT_NAME 
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''


# SOUTH

SOUTH_AUTO_FREEZE_APP = True


# TINYMCE

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "paste",
    'theme': "advanced",
    'custom_shortcuts': False,
    'object_resizing': False,
    'height': 400,
    'theme_advanced_blockformats': "p,h2,h3",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_buttons1': "bold,italic,underline,separator,justifyleft,justifycenter,justifyright,justifyblock,separator,bullist,numlist,outdent,indent,separator,undo,redo,separator,formatselect,removeformat,cleanup,separator,link,unlink,image,separator,code",
    'theme_advanced_buttons2': "",
    'theme_advanced_buttons3': "",
    'content_css': MEDIA_URL + 'css/screen.css',
}


# FILEBROWSER

FILEBROWSER_URL_WWW = '/media/files/'
FILEBROWSER_PATH_SERVER = os.path.join(MEDIA_ROOT, 'files')
FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
FILEBROWSER_EXTENSIONS = {
    'Folder':[''],
    'Image':['.jpg', '.jpeg', '.gif','.png','.tif','.tiff'],
    'Video':['.mov','.wmv','.mpeg','.mpg','.avi','.rm','.flv','.swf'],
    'Document':['.pdf','.doc','.rtf','.txt','.xls','.csv'],
    'Sound':['.mp3','.mp4','.wav','.aiff','.midi'],
}
FILEBROWSER_MAX_UPLOAD_SIZE = 100000000
FILEBROWSER_USE_IMAGE_GENERATOR = True
FILEBROWSER_IMAGE_GENERATOR_LANDSCAPE = [('small_',160),('medium_',320),('large_',640),('huge_',800)]
FILEBROWSER_IMAGE_GENERATOR_PORTRAIT = [('small_',160),('medium_',320),('large_',640),('huge_',640)]
FILEBROWSER_IMAGE_CROP_GENERATOR = [('crop_small_',80,80),('crop_medium_',160,160)]



try:
    execfile(os.path.join(os.path.dirname(__file__), "settings_local.py"))
except IOError:
    pass
