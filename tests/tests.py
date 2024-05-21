import pytest
from django.urls import reverse, reverse_lazy

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize(
    "url",
    [
        reverse_lazy("account_login"),
        reverse_lazy("account_reset_password"),
        reverse_lazy("account_email_verification_sent"),
    ],
)
def test_200_all_urls(url, client):
    res = client.get(url)
    assert res.status_code == 200


def test_works_without_socialaccount_app(settings, client):
    settings.INSTALLED_APPS = [
        app for app in settings.INSTALLED_APPS if app != "allauth.socialaccount"
    ]
    res = client.get(reverse("account_login"))
    assert res.status_code == 200
