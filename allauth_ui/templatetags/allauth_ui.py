from django import template
from django.conf import settings
from slippers.templatetags.slippers import register_components

register = template.Library()


@register.simple_tag
def allauth_ui_theme():
    return settings.ALLAUTH_UI_THEME


register_components(
    {
        "container": "components/container.html",
        "form": "components/form.html",
    },
    register,
)
