# settings.py for Django project

INSTALLED_APPS = [
    # ...existing apps...
    'djongo',
    'octofit_tracker',
]

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[zany-space-zebra-4675vp697x627qpr]-8000.app.github.dev']

# Adicionar configuração para evitar problemas de HTTPS
SECURE_SSL_REDIRECT = False
CSRF_TRUSTED_ORIGINS = ['https://[zany-space-zebra-4675vp697x627qpr]-8000.app.github.dev']

# Other settings...

# Add any additional configurations as needed.