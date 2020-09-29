from django.apps import AppConfig

class NewspapersConfig(AppConfig):
    name = 'newspapers'

    def ready(self):
        from forecastUpdater import updater
        updater.start()
