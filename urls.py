from django.conf.urls.defaults import *
from django.contrib import admin

from healingcirclemassage.settings import MEDIA_ROOT
from healingcirclemassage.static.models import Service, Faq



admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'home.html'}),
    (r'^consultation/$', 'direct_to_template', {'template': 'consultation.html'}),
    (r'^resume/$', 'direct_to_template', {'template': 'resume.html'}),
    (r'^intake/$', 'direct_to_template', {'template': 'intake.html'}),
    (r'^help/$', 'direct_to_template', {'template': 'help.html'}),
)

urlpatterns += patterns('django.views.generic.list_detail',
    (r'^services/$', 'object_list',{'queryset': Service.objects.all(), 'template_name': 'services.html'}),
    (r'^faq/$', 'object_list',{'queryset': Faq.objects.all(), 'template_name': 'faq.html'}),
)

urlpatterns += patterns('',
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    (r'^admin/(.*)$', admin.site.root),
)
