from pathlib import Path

# ==================================================
#   المسارات الأساسية
# ==================================================
BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
#   الإعدادات العامة
# ==================================================
SECRET_KEY = 'django-insecure-1cfo^a#)$rh3l=spjcze5%ku$*=*v!68x%2spqm8cp-i9ac9o7'

DEBUG = True

ALLOWED_HOSTS = []


# ==================================================
#   التطبيقات
# ==================================================
INSTALLED_APPS = [
    # Django Core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project Apps
    'store',
    'cart',
    'accounts',
]


# ==================================================
#   Middlewares
# ==================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Sessions
    'django.contrib.sessions.middleware.SessionMiddleware',

    # دعم اللغة العربية
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',

    # CSRF Protection
    'django.middleware.csrf.CsrfViewMiddleware',

    # Authentication
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # Messages
    'django.contrib.messages.middleware.MessageMiddleware',

    # Clickjacking Protection
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==================================================
#   إعدادات الروابط
# ==================================================
ROOT_URLCONF = 'proj5.urls'


# ==================================================
#   القوالب Templates
# ==================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # مجلد القوالب العام
        'DIRS': [
            BASE_DIR / 'templates',
        ],

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


# ==================================================
#   WSGI
# ==================================================
WSGI_APPLICATION = 'proj5.wsgi.application'


# ==================================================
#   قاعدة البيانات
# ==================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==================================================
#   التحقق من كلمات المرور
# ==================================================
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


# ==================================================
#   اللغة والتوقيت
# ==================================================
LANGUAGE_CODE = 'ar'

TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_L10N = True
USE_TZ = False


# ==================================================
#   الملفات الثابتة Static
# ==================================================
STATIC_URL = '/static/'

# ملفات static الخاصة بالمشروع
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# مكان التجميع عند collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ==================================================
#   ملفات الوسائط Media
# ==================================================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==================================================
#   إعدادات الأمان (مناسبة للتطوير)
# ==================================================
X_FRAME_OPTIONS = 'DENY'

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True


# ==================================================
#   الإعدادات الافتراضية
# ==================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
