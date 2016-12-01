from django.db import models

class Family(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    grandchildren = models.TextField()
    pets = models.TextField()
    comments1 = models.TextField()
    comments2 = models.TextField()
    children = models.TextField()
    member_since = models.DateField()


class Person(models.Model):
    family = models.ForeignKey(Family)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email1 = models.EmailField()
    email2 = models.EmailField()
    phone1 = models.CharField(max_length=30)
    phone2 = models.CharField(max_length=30)
    contact_notes = models.TextField()
    executive = models.BooleanField()
    leadership = models.BooleanField()
    jcs = models.BooleanField()

    MEMBER = 'M'
    VISITOR = 'V'
    REMOVED = 'R'
    STATUS_CHOICES = (
        (MEMBER, 'Member'),
        (VISITOR, 'Visitor'),
        (REMOVED, 'Removed'),
    )

    status = models.CharField(max_length=1, choices = STATUS_CHOICES, default=MEMBER)

    newsletter_by_mail = models.BooleanField()


