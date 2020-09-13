import pytest

from project.app.models import Resource


@pytest.mark.django_db
def test_resource_init():
    test_key = "vcard/ratio20/images/card/1e4d1285f407353efd1c5f209d1955e2.jpg"
    test_url = "https://dqx9mbrpz1jhx.cloudfront.net/" + test_key
    model = Resource(url=test_url)
    assert model.key == test_key
