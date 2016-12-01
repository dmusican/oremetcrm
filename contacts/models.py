from django.db import models

class Family(models.Model):
    family_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    grandchildren = models.TextField(blank=True, null=True)
    pets = models.TextField(blank=True, null=True)
    comments1 = models.TextField(blank=True, null=True)
    comments2 = models.TextField(blank=True, null=True)
    children = models.TextField(blank=True, null=True)
    member_since = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.family_name


class Person(models.Model):
    family = models.ForeignKey(Family)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    phone1 = models.CharField(max_length=30, blank=True, null=True)
    phone2 = models.CharField(max_length=30, blank=True, null=True)
    contact_notes = models.TextField(blank=True, null=True)
    executive = models.BooleanField(default=False)
    leadership = models.BooleanField(default=False)
    jcs = models.BooleanField(default=False)

    MEMBER = 'M'
    VISITOR = 'V'
    REMOVED = 'R'
    STATUS_CHOICES = (
        (MEMBER, 'Member'),
        (VISITOR, 'Visitor'),
        (REMOVED, 'Removed'),
    )
    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default=MEMBER)

    newsletter_by_mail = models.BooleanField(default=False)

    def __unicode__(self):
        return self.last_name + ", " + self.first_name

