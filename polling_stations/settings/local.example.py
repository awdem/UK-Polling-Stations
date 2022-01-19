DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "polling_stations",
        "USER": "postgres",
        "PASSWORD": "",
        "HOST": "",  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        "PORT": "",  # Set to empty string for default.
    }
}

EVERY_ELECTION = {"CHECK": False, "HAS_ELECTION": True}
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
