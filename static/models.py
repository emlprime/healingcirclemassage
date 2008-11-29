from django.db import models


class Service(models.Model):

    CATEGORY_CHOICES = (
        ("M","Massage Services"),
        ("O","Other Services"),
        )


    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="images", null=True, blank=True)

    def __unicode__(self):
        return self.name

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __unicode__(self):
        return self.question

class News_item(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to="images")

    def __unicode__(self):
        return self.name

class Writing(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

class Testimonial(models.Model):
    description = models.TextField()
    source = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.source
