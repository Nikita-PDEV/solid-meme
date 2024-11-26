import os  
from pathlib import Path  

# Путь к корневой директории проекта  
BASE_DIR = Path(__file__).resolve().parent.parent  

# Генерация секретного ключа (не для использования в продакшене)  
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secret-key')  

# Включение режима отладки  
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'  

ALLOWED_HOSTS = []  # разрешенные хосты  

# Приложения, которые используются в проекте  
INSTALLED_APPS = [  
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',  
    'django.contrib.sites',   
    'allauth',  
    'allauth.account',  
    'allauth.socialaccount',   
    'news',    
]  


SITE_ID = 1  

# Middleware для обработки запросов  
MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',  
    'django.contrib.sessions.middleware.SessionMiddleware',  
    'django.middleware.common.CommonMiddleware',  
    'django.middleware.csrf.CsrfViewMiddleware',  
    'django.contrib.auth.middleware.AuthenticationMiddleware',  
    'django.contrib.messages.middleware.MessageMiddleware',  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  
    'allauth.account.middleware.AccountMiddleware',  
]  

# Корневой URL-адрес конфигурации  
ROOT_URLCONF = 'news_portal.urls'  

# Шаблоны  
TEMPLATES = [  
    {  
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  
        'DIRS': [],  
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

# Конфигурация WSGI  
WSGI_APPLICATION = 'news_portal.wsgi.application'  

# База данных  
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.sqlite3',  # можно изменить на другую БД, например, PostgreSQL  
        'NAME': BASE_DIR / 'db.sqlite3',  
    }  
}  

# Пароли  
AUTH_PASSWORD_VALIDATORS = [  
    {  
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  
    },  
    {  
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  
        'OPTIONS': {  
            'min_length': 8,  
        },  
    },  
    {  
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  
    },  
    {  
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  
    },  
]  

# Язык и часовой пояс  
LANGUAGE_CODE = 'en-us'  
TIME_ZONE = 'UTC'  
USE_I18N = True  
USE_L10N = True  
USE_TZ = True  

# Статические файлы (CSS, JavaScript, изображения)  
STATIC_URL = '/static/'  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Если есть статические файлы в этой папке  

# Медиа файлы (загружаемые пользователями)  
MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  

# Настройки для django-allauth  
LOGIN_REDIRECT_URL = '/'  
ACCOUNT_EMAIL_VERIFICATION = 'none'    

# Настройки для отправки электронной почты (пример с Gmail)  
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True  
EMAIL_HOST_USER = os.environ.get('nikitavaul228556@gmail.com')  # Ваша электронная почта  
EMAIL_HOST_PASSWORD = os.environ.get('plm321qaz')  # Ваш пароль  

# Default primary key field type  
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field  
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  