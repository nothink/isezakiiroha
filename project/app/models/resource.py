from django.core.validators import RegexValidator
from django.db import models


class Resource(models.Model):
    """vcardサーバから取得したリソースを管理するモデルクラス"""

    validate_safe_key = RegexValidator(
        regex=r"^[0-9a-zA-Z:!/()*'.%@_-]+",
        message=("This key isn't a safe key for S3/GCS."),
    )
    vakudate_vcard_key = RegexValidator(
        regex=r"^vcard/",
        message=("This key isn't a vcard resource"),
    )

    key = models.CharField(
        max_length=1024,
        null=False,
        blank=False,
        db_index=True,
        editable=False,
        unique=True,
        validators=[validate_safe_key, vakudate_vcard_key],
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key
