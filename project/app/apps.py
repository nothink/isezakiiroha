from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    """API用のAppConfig"""

    name = "project.app"

    def ready(self):
        """readyメソッドでsignalを読み込ませている"""
        from project.app import signals  # noqa
