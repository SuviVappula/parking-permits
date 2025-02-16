from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import TimestampedModelMixin, UUIDPrimaryKeyMixin


class DrivingClass(TimestampedModelMixin, UUIDPrimaryKeyMixin):
    class_name = models.CharField(_("Driving class name"), max_length=32)
    identifier = models.CharField(_("Driving class identifier"), max_length=32)

    class Meta:
        verbose_name = _("Driving class")
        verbose_name_plural = _("Driving classes")

    def __str__(self):
        return "%s - %s" % (self.class_name, self.identifier)
