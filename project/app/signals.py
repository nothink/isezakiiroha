import urllib.request

from django.db.models.signals import pre_save
from django.dispatch import receiver

from project.app.models import Resource


@receiver(pre_save, sender=Resource)
def create_user_profile(sender, instance, **kwargs):
    # TODO: ここでfetchしてGCPに送りつける
    print(instance.url)

    req = urllib.request.Request(instance.url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    print(len(body))
    with open("tmp_gfiku.jpg", "wb") as f:
        f.write(body)
