from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import mail_admins
from django.template import RequestContext
from django.shortcuts import render_to_response


from healingcirclemassage.static.models import Appointment
from healingcirclemassage.static.forms import AppointmentForm


def appointment(request):
    """ Creates an appointment object and emails to Kathy from the appointment form
    """
    template = "appointment.html"
    if request.method == 'POST':
        values = request.POST.copy()
        form = AppointmentForm(values)
        if form.is_valid():
            appointment=form.save()
            message =  "%s %s\n%s\n%s\n%s" % (appointment.first_name, appointment.last_name, appointment.phone_number, appointment.email, appointment.description)
            # try to send mail. If it fails print out an error
            try:
                mail_admins('Appointment Request Submitted', message, fail_silently=False)
            except:
                print "Error: could not send mail to admins"
            return HttpResponseRedirect("/appointment/create/")
        else:
            errors=form.errors
    else:
        form = AppointmentForm()
    context = locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

