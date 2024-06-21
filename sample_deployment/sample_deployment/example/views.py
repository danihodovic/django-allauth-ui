import json

from allauth.socialaccount.models import SocialAccount
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "example/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            social_account = SocialAccount.objects.filter(  # pylint: disable=no-member
                user=self.request.user
            ).first()
            if social_account:
                context["extra_data"] = social_account.extra_data
        return context


class SocialAccountMetadataView(TemplateView):
    template_name = "example/social_metadata.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            social_account = SocialAccount.objects.filter(  # pylint: disable=no-member
                user=self.request.user
            ).first()
            if social_account:
                context["extra_data"] = social_account.extra_data
                json_str = json.dumps(social_account.extra_data, indent=2)
                as_code_block = []
                for line in json_str.split("\n"):
                    as_code_block.append(f"<pre ><code>{line}</code></pre>")
                context["code_block"] = "\n".join(as_code_block)
        return context


home_view = HomePageView.as_view()
social_account_metadata_view = SocialAccountMetadataView.as_view()
