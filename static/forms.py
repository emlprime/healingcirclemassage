from django.forms.models import ModelForm
from django.forms import forms

from healingcirclemassage.static.models import Appointment, Email

class AppointmentForm(ModelForm):
    """ Provides the appointment request form
    """

    class Meta:
        model = Appointment

    def save(self, commit=True):
        appointment = super(AppointmentForm, self).save()
        return appointment

class EmailForm(ModelForm):
    """Provides the form for adding emails to the mailing list
    """
    class Meta:
        model = Email

    def save(self, commit=True):
        email = super(EmailForm, self).save()
        return email
