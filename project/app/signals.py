import io
import urllib.request

from django.db.models.signals import pre_save
from django.dispatch import receiver
from google.cloud import storage

from project.app.models import Resource


@receiver(pre_save, sender=Resource)
def fetch_and_upload_resource(sender, instance, **kwargs):
    """
    作成されたリソースをもとにリソース回収をはかり、GCSのbucketに格納する
    """

    try:
        req = urllib.request.Request(instance.url)
        with urllib.request.urlopen(req) as res:
            body = res.read()
        buf = io.BytesIO(body)
        buf.seek(0)
        client = storage.Client()
        blob = client.bucket("irohasan").blob(instance.key)
        blob.upload_from_file(buf)
        instance.fetched = True
    except Exception as e:
        # なんらかのログを吐くべき
        print(e)
