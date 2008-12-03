from django.db import models


class Appointment(models.Model):
    """ Model for the appointment requests submitted on the appointments page
    """

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 20)
    email = models.EmailField()
    description = models.TextField()

    def __unicode__(self):
        return self.last_name()


class Resume(models.Model):
    employment = models.TextField()
    training_and_education = models.TextField()
    professional = models.TextField()
    personal_interests = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.employment

class Home_text(models.Model):
    text = models.TextField()
    date = models.DateField()

    def __unicode__(self):
        return self.text

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
    link = models.CharField(max_length = 255, null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to="images", null=True, blank=True)
    image_1 = models.ImageField(upload_to="images", null=True, blank=True)
    image_2 = models.ImageField(upload_to="images", null=True, blank=True)
    image_3 = models.ImageField(upload_to="images", null=True, blank=True)
    image_4 = models.ImageField(upload_to="images", null=True, blank=True)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to="images")

    def __unicode__(self):
        return self.name

class Writing(models.Model):
    name = models.CharField(max_length = 255)
    link = models.CharField(max_length = 255, null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to="images", null=True, blank=True)
    image_1 = models.ImageField(upload_to="images", null=True, blank=True)
    image_2 = models.ImageField(upload_to="images", null=True, blank=True)
    image_3 = models.ImageField(upload_to="images", null=True, blank=True)
    image_4 = models.ImageField(upload_to="images", null=True, blank=True)

    def __unicode__(self):
        return self.name

class Testimonial(models.Model):
    description = models.TextField()
    source = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.source
