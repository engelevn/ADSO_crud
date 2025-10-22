"""
Django settings for tecnopunto project.
Guía oficial CRUD TecnoPunto - ADSO 2025
"""

from pathlib import Path

# BASE_DIR identifica la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta (no compartir en producción)
SECRET_KEY = 'django-insecure-9dvnkfi_ajh_7f4zj^$+#g_drxjn#-yogg#3shas88hu16^s%!'

# Modo desarrollo
DEBUG = True

ALLOWED_HOSTS = []


# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',  # nuestra app del CRUD
]


# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URL principal del proyecto
ROOT_URLCONF = 'tecnopunto.urls'


# Templates: donde Django buscará los HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta global donde está base.html
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


WSGI_APPLICATION = 'tecnopunto.wsgi.application'


# =======================
# 🛠️ CONFIGURACIÓN MYSQL
# =======================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tecnopunto_db',
        'USER': 'root',
        'PASSWORD': '',  # o tu contraseña de MySQL si tienes una
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        }
    }
}






# =======================
# 🔐 VALIDACIÓN DE CONTRASEÑAS
# =======================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# =======================
# 🌍 INTERNACIONALIZACIÓN
# =======================
LANGUAGE_CODE = 'es-co'  # español colombiano
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


# =======================
# 📁 ARCHIVOS ESTÁTICOS
# =======================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # carpeta donde están CSS, JS e imágenes
STATIC_ROOT = BASE_DIR / 'staticfiles'    # destino de collectstatic


# =======================
# 📄 CONFIGURACIÓN EXTRA
# =======================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


