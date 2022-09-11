DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'threepldashboard',
        'USER': 'threepluser',
        'PASSWORD': 'threeplpassword',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

HONEYBADGER = {
    'API_KEY': 'hbp_iM6vJaJ3jO4dKUcrAfCrSxvgtFeVpV3P0eYY',
    'force_report_data': True
}

SENDGRID_API = "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"
FROM_EMAIL = "k.ahmed2k19@gmail.com"
SERVER_URL = "127.0.0.1:8000"

# import os
#
# DATABASE = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # 'NAME': 'premiere',
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': os.environ.get('POSTGRES_HOST'),
#         'PORT': os.environ.get('POSTGRES_PORT'),
#     }
# }
#
# HONEYBADGER = {
#     'API_KEY': os.environ.get('HONEYBADGER_API_KEY'),
#     'force_report_data': True
# }
#
#
# SENDGRID_API = "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"
# FROM_EMAIL = "k.ahmed2k19@gmail.com"
# SERVER_URL = "127.0.0.1:8000"