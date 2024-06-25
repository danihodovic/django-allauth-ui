from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def allauth_ui_theme():
    return settings.ALLAUTH_UI_THEME
