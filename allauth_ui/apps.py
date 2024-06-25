from django.apps import AppConfig


class AllauthUiConfig(AppConfig):
    name = "allauth_ui"

    def ready(self):
        # pylint: disable=import-outside-toplevel
        from django.conf import settings

        settings.ALLAUTH_UI_THEME = getattr(settings, "ALLAUTH_UI_THEME", "light")
