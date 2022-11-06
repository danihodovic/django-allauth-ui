import djclick as click
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers import registry
from django.contrib.sites.models import Site


@click.command()
def command():
    click.secho("Purging existing providers...")
    SocialApp.objects.all().delete()
    for provider_name, provider_label in registry.as_choices():
        app = SocialApp(
            provider=provider_name,
            name=provider_label,
            client_id="x",
            secret="y",
        )
        app.save()
        app.sites.set(Site.objects.all())
        click.secho(f"Created {app}", fg="green")
