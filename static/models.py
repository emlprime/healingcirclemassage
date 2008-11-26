from django.db import models

class Service(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.TextField()

    def unicode(self):
        return name

class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def unicode(self):
        return question

class News_item(models.Model):
    name = models.CharField(max_length = 255)

    def unicode(self):
        return name

class Event(models.Model):
    name = models.CharField(max_length = 255)

    def unicode(self):
        return name

class Writing(models.Model):
    name = models.CharField(max_length = 255)

    def unicode(self):
        return name

class Testimonial(models.Model):
    description = models.TextField()
    
    def unicode(self):
        return description
