import os

gettext = lambda s: s

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ("Anatoly Bubenkov", "bubenkoff@gmail.com"),
)

LOCAL_DEV = True

SERVER_EMAIL = "noreply@django-dev.zojax.com"

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'zojax_com.db'
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', gettext('English')),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Static file configuration
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'media', 'static')
STATIC_URL = MEDIA_URL + 'static/'
STATICFILES_EXCLUDED_APPS = (
    'project',
)
STATICFILES_MEDIA_DIRNAMES = (
    'media',
    'static',
)
STATICFILES_PREPEND_LABEL_APPS = (
    'django.contrib.admin',
    'pages',
    'articles',
)
STATICFILES_DIRS = (
    ('satchmo', 'parts/satchmo/satchmo/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',)

ADMIN_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'admin_media')
ADMIN_MEDIA_PREFIX = '/admin_media/'

PAGES_MEDIA_URL = STATIC_URL + "pages/pages/"

TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'tiny_mce')
TINYMCE_FILEBROWSER = True

FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL + "filebrowser/"
FILEBROWSER_PATH_MEDIA = os.path.join(STATIC_ROOT, 'filebrowser')

FILEBROWSER_URL_TINYMCE = STATIC_URL + 'tiny_mce/'
FILEBROWSER_PATH_TINYMCE = TINYMCE_JS_ROOT

FEINCMS_ADMIN_MEDIA = STATIC_URL + 'feincms/'

ADMINFILES_MEDIA_URL = STATIC_URL

FLASH_IGNORE_MEDIA = True # Optional. Default: DEBUG
FLASH_STORAGE = 'session' # Optional

# Don't share this with anybody.
SECRET_KEY = 'safeplace5k^z@_&q1cpy_yypx$firv#qtgo%h+xnov@vrab95'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #"django.middleware.csrf.CsrfViewMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'djangoflash.middleware.FlashMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.doc.XViewMiddleware',
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    #'project.middleware.SSLRedirect',
    'django.middleware.transaction.TransactionMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'project.urls'


INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.messages',
    'satchmo_store.shop',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.humanize',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.syndication',
    'django_extensions',
    'kss.django',
    'south',
    'staticfiles',
    'compressor',
    'robots',
    'debug_toolbar',
    'tinymce',
    'filebrowser',
    'mptt',
    'pages',
    'registration',
    'adminfiles',
    'flatblocks',
    'storages',
    'treemenus',
    'articles',
    'keyedcache',
    'livesettings',
    'authority',
    'l10n',
    'sorl.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    'product',
    'product.modules.configurable',
    'product.modules.custom',
    'product.modules.subscription',
    'product.modules.downloadable',
    'payment',
    #'payment.modules.giftcertificate',
    'payment.modules.paypal',
    'payment.modules.authorizenet',
    #'payment.modules.google',
    'satchmo_utils',
    'app_plugins',

    'zojax.django.blueprint',
    'zojax.django.jquery',
    'zojax.django.mailin',
    'zojax.django.widgets.datetime',
    'zojax.django.extendedmenus',
    'zojax.django.extendedflatblocks',
    'zojax.django.forms',
    'vdr',
    'profile',
    'authentication',
    'project',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

SITE_ID = 1

TEMPLATE_CONTEXT_PROCESSORS = (
    'satchmo_store.shop.context_processors.settings',
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.contrib.messages.context_processors.messages',
    'djangoflash.context_processors.flash',
    'staticfiles.context_processors.static_url',
    'pages.context_processors.media',
)

MESSAGES_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


DEFAULT_PAGE_TEMPLATE = 'pages/default.html'
PAGE_LANGUAGES = (
    ('en-us', gettext('US English')),
)
PAGE_REAL_TIME_SEARCH = False
PAGE_TAGGING = False
PAGE_TINYMCE = True


DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter',
                        'compressor.filters.csstidy.CSSTidyFilter']
COMPRESS_CSSTIDY_BINARY = '/usr/bin/csstidy'
COMPRESS_CSSTIDY_ARGUMENTS = '--template=highest  --remove_last_;=true  --sort_properties=false  --sort_selectors=false  --merge_selectors=1'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'width' : "60%",
    'height' : "400"
}
TINYMCE_SPELLCHECKER = True

LOGIN_REDIRECT_URL = "/vdr/browse/"

from pytils.translit import slugify

AUTOSLUG_SLUGIFY_FUNCTION = lambda x: slugify(x.strip())

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CRYPTO_KEYS_PUB = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'parts', 'keys', 'pub.key')

CRYPTO_KEYS_PRIV = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'parts', 'keys', 'priv.key')

AWS_DEFAULT_ACL = 'private'
AWS_HEADERS = {'Content-Disposition': 'attachment'}

HTTPS_PATHS = (
    #'admin/', temporary due to flash ssl issue
    'accounts/',
    'management/',
    'checkout/',
    'settings/',
    'cache/',
    'vdr/',
    'kss/'
)

HTTPS_SUPPORT = True

import kss.django
try:
    kss.django.activate('kss-core', 'inlinejs')
except KeyError:
    pass

import mimetypes

mimetypes.add_type('text/plain', '.kss')

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

#### Satchmo unique variables ####
#from django.conf.urls.defaults import patterns, include
SATCHMO_SETTINGS = {
                    'SHOP_BASE' : '',
                    'MULTISHOP' : False,
                    'SSL'       : False,
                    #'SHOP_URLS' : patterns('satchmo_store.shop.views',)
                    }

from kss.base import config
config.third_party_js = [
    'sarissa.js',
]

config.KSSCore.extra_javascripts = [os.path.join(config.kukit_dir, '3rd_party', f)
                         for f in config.third_party_js]


from kss.django.templatetags import ksstags

old_render = ksstags.KSSExtraScriptsNode.render

def render(self, context):
    return """\n<script type="text/javascript" >
if (typeof cssQuery == 'undefined') {
    function cssQuery(s, f) { return jQuery.makeArray(jQuery(s, f)) };
};
</script>"""+old_render(self, context)

ksstags.KSSExtraScriptsNode.render = render
# Load the local settings

from local_settings import *

import site_logging
