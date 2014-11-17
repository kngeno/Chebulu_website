
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "20e1b629-3343-4195-8ff8-6ec2c51070881a2d1dcf-17c7-447a-994c-281946fc4eceaf95c53f-79e9-41f4-83f7-b5ab5b961911"
NEVERCACHE_KEY = "b1a2ff45-8376-4d69-bddd-265ad2b46c9a9d6b44dd-f4d2-43e4-a450-85ac6e04e4ce0d633941-39df-4f23-afb2-7cae75dd7cc5"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
