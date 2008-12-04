from django.contrib import admin
from healingcirclemassage.static.models import Service, Faq, News_item, Event, Writing, Testimonial, Resume, Home_text, Appointment

class ResumeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Resume, ResumeAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class Home_textAdmin(admin.ModelAdmin):
    pass
admin.site.register(Home_text, Home_textAdmin)

class ServiceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Service, ServiceAdmin)

class FaqAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faq, FaqAdmin)

class News_itemAdmin(admin.ModelAdmin):
    pass
admin.site.register(News_item, News_itemAdmin)

class EventAdmin(admin.ModelAdmin):
    pass
admin.site.register(Event, EventAdmin)

class WritingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Writing, WritingAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    pass
admin.site.register(Testimonial, TestimonialAdmin)
