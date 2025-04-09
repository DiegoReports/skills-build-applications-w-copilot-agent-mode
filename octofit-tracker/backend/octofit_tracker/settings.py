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

# Other settings...

# Add any additional configurations as needed.