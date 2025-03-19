from django.apps import AppConfig


class InsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insapp'


#this needs to be registered
#"insapp.apps.InsappConfig"