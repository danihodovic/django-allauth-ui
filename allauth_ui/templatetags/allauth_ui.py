import re
from pathlib import Path
from allauth.socialaccount.models import SocialAccount

from django import template


register = template.Library()

input_css_path = Path(__file__).parent / ".." / "static" / "allauth_ui" / "input.css"
social_colors = []

with open(input_css_path, encoding="utf8") as f:
    for line in f.readlines():
        m = re.search(r"\.social-(?P<provider>\w+)\s?", line)
        if m:
            social_colors.append(m.groupdict()["provider"])


@register.filter()
def socialprovider_color(socialprovider):
    name = socialprovider.name.lower()
    if name in social_colors:
        return f"social-{name}"
    return "bg-stone-900 hover:bg-black"


@register.simple_tag
def provider_connected(socialprovider, user):
    if not user.is_authenticated:
        return False
    # pylint: disable=no-member
    return bool(
        SocialAccount.objects.filter(provider=socialprovider.name.lower(), user=user)
    )
