from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    name = "project.app"

    def ready(self):
        from project.app import signals  # noqa
