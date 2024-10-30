from pathlib import Path
import os.path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-88)5ylc$&!#l7%0$oq&bdfn$*gzc#!-sk+*yj(216bb7-aq%y2'
DEBUG = True
ALLOWED_HOSTS = []


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

ROLESPERMISSIONS_MODULE = 'app.roles'



# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adm',
    'cliente',
    'produto',
    'register',
    'acompanhamento',
    'tuper',
    'faturamento',
    'home',
    'rolepermissions',
    'login',
    'requisicao',
    'manutencaolist',
    'reativacao',
    'qualit',
    'formulariov',
    'formularioe',
    'usuarios',     
    'estoque',     
    'registrodemanutencao',
    'saidas',
    'formacompanhamento',    
    'prestadores',    
    'regcliente',    
    'dashboard',    
    'IAO',   
    't42', 
    'pparada', 
    'ticket', 
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Adicione este middleware
]

ROOT_URLCONF = 'app.urls'

ALLOWED_HOSTS = ['10.0.0.227', 'localhost', '10.0.0.196']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Atualizado para pasta templates na raiz
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LOGOUT_REDIRECT_URL ="/"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATE_INPUT_FORMATS = ['%d/%m/%Y']
DATE_FORMAT = 'd/m/Y'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sysggoldensat@gmail.com'
EMAIL_HOST_PASSWORD = 'yzxs ieko subp xesu'

LOGIN_REDIRECT_URL = 'home'  # Nome da URL para redirecionar após login
LOGOUT_REDIRECT_URL = 'login'  # Nome da URL para redirecionar após logout
LOGIN_URL = 'login'
# Verifique se 'login' está corretamente configurado e inclui a URL para login.
ROLESPERMISSIONS_MODULE = 'app.roles'  # Certifique-se de que o caminho está correto
