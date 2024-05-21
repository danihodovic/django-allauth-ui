import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_works_without_socialaccount_app(settings, client):
    settings.INSTALLED_APPS = [
        app for app in settings.INSTALLED_APPS if app != "allauth.socialaccount"
    ]
    res = client.get(reverse("account_login"))
    assert res.status_code == 200
