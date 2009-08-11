from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.template import RequestContext
from django.shortcuts import render_to_response


from healingcirclemassage.static.models import Appointment, Resume, HomeText, NewsItem, Interview, WritingTestimonial, Writing, ContributingWriter, DVDTestimonial
from healingcirclemassage.static.forms import AppointmentForm, EmailForm

def dvd_page(request):
    template='instructional_dvd.html'
    testimonials = DVDTestimonial.objects.all()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))


def writings(request):
    template = 'writing.html'
    other = ContributingWriter.objects.filter(publication="O")
    bizchicksrule = ContributingWriter.objects.filter(publication="B")
    massagemagazine = ContributingWriter.objects.filter(publication="M")
    southwestblend = ContributingWriter.objects.filter(publication="S")        
    articles = Writing.objects.all()
    testimonials = WritingTestimonial.objects.all()
    context = locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def news_items(request):
    """Submits both the news_items list and the interviews list to the news page
    """
    template = 'inthenews.html'
    news_items = NewsItem.objects.all()
    interviews = Interview.objects.all()
    context = locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def resume(request):
    """Submits the latest resume to the URL
    """
    template = "resume.html"
    resume = Resume.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def speaking(request):
    """ Bio and bullet points of lectures with testmonials
    """
    template = "speaking.html"
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def hometext(request):
    """Submits the latest hometext to the URL
    """
    template = "home.html"
    hometext = HomeText.objects.latest()
    context=locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

def email_add(request):
    """ Creates an email object and notifies Kathy that she has a new email subscriber
    """
    if request.method=='POST':
        print "request method is post"
        page = request.META['HTTP_REFERER'] if request.META.has_key('HTTP_REFERER') else '/'
        values = request.POST.copy()
        print values
        form=EmailForm(values)
        if form.is_valid():
            print "form is valid"
            email=form.save()
            message = "%s has subscribed to your email mailing list" % (email)
            #try to send mail. If it fails, print an error
            try:
                send_mail('Email Subscriber to Healing Circle', message, 'subscribers@healingcirclemassage.com', ['healingcirclemassage@hotmail.com'], fail_silently=False)
            except:
                print "Error: could not send mail"
        else:
            print "form is not valid", form.errors
            errors = form.errors
    context=locals()
    return HttpResponseRedirect(page)


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
                send_mail('Appointment Request Submitted', message, 'appointments@healingcirclemassage.com', ['healingcirclemassage@hotmail.com'], fail_silently=False)
            except:
                print "Error: could not send mail to admins"
            return HttpResponseRedirect("/appointment/confirm/")
        else:
            errors=form.errors
    else:
        form = AppointmentForm()
    context = locals()
    return render_to_response(template, context, context_instance=RequestContext(request))

