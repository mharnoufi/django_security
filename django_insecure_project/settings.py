from pathlib import Path
import os
from csp.constants import SELF
from dotenv import load_dotenv

load_dotenv()

# Variable pour activer le mode sécurisé
DJANGO_SECURE = os.getenv("DJANGO_SECURE","false").lower() == "true"

# En production, DEBUG doit être False
DEBUG = not DJANGO_SECURE

# Domaine autorisés
ALLOWED_HOSTS = ["127.0.0.1","localhost"]

# Pour HTTPS local sur port 8443
CSRF_TRUSTED_ORIGINS = [
    "https://127.0.0.1",
    "https://localhost",
    "https://127.0.0.1:8443",
]

# Cookies en HTTPS uniquement
SESSION_COOKIE_SECURE = DJANGO_SECURE
CSRF_COOKIE_SECURE = DJANGO_SECURE

# Interdire l’accès JS (XSS)
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True  

# CSRF (défaut raisonnable)
SESSION_COOKIE_SAMESITE = "Lax"  # adapte si besoin (iframe/OAuth)
CSRF_COOKIE_SAMESITE = "Lax"

# HTTPS et HSTS 
SECURE_SSL_REDIRECT = DJANGO_SECURE
SECURE_HSTS_SECONDS = 31536000 if DJANGO_SECURE else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # False si sous domaine en HTTP
SECURE_HSTS_PRELOAD = DJANGO_SECURE # True en prod si 100% HTTPS

# Protection contre le MIME sniffing
SECURE_CONTENT_TYPE_NOSNIFF = True

# Contrôle du header Referer
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Protection contre le clickjacking
X_FRAME_OPTIONS = "DENY"


#CSP stricte : n'autorise que les ressources de notre domaine
CONTENT_SECURITY_POLICY = {
    "EXCLUDE_URL_PREFIXES": ["/admin"], 
    "DIRECTIVES": {
        "default-src": [SELF],     
        "script-src": [SELF],          
        "style-src": [SELF],              
        # "img-src": [SELF, "data:"],
    },
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-insecure-key")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "csp",
    "sslserver",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_insecure_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_insecure_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
