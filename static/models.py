from django.db import models

class Service(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.TextField()

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
