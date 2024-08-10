from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_view, name='about'),  # Ensure this matches the name used in templates
    path('academic/', views.Academic, name='academic'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('hire-me/', views.hire_me_view, name='hire_me'),
    path('success/', views.success, name='success'), 
    path('resume/', views.resume_page_view, name='resume_page'),
]
if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)