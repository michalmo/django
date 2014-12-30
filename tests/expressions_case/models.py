from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class CaseTestModel(models.Model):
    integer = models.IntegerField()
    integer2 = models.IntegerField()
    string = models.CharField(max_length=100)

    big_integer = models.BigIntegerField(null=True)
    binary = models.BinaryField(null=True)
    boolean = models.BooleanField(default=False)
    comma_separated_integer = models.CommaSeparatedIntegerField(max_length=100, null=True)
    date = models.DateField(null=True)
    date_time = models.DateTimeField(null=True)
    decimal = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    duration = models.DurationField(null=True)
    email = models.EmailField(null=True)
    file = models.FileField(null=True)
    file_path = models.FilePathField(null=True)
    float = models.FloatField(null=True)
    image = models.ImageField(null=True)
    ip_address = models.IPAddressField(null=True)
    generic_ip_address = models.GenericIPAddressField(null=True)
    null_boolean = models.NullBooleanField()
    positive_integer = models.PositiveIntegerField(null=True)
    positive_small_integer = models.PositiveSmallIntegerField(null=True)
    slug = models.SlugField(null=True)
    small_integer = models.SmallIntegerField(null=True)
    text = models.TextField(null=True)
    time = models.TimeField(null=True)
    url = models.URLField(null=True)
    uuid = models.UUIDField(null=True)
    fk = models.ForeignKey('self', null=True)

    def __str__(self):
        return "%i, %s" % (self.integer, self.string)


@python_2_unicode_compatible
class FKCaseTestModel(models.Model):
    fk = models.OneToOneField(CaseTestModel, related_name='fk_rel')
    integer = models.IntegerField()

    def __str__(self):
        return "%i, %s" % (self.id, self.fk)
