from django.urls import path
from app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('why_us/', why_us, name='why_us'),
    path('contact/', contact, name='contact'),
    path('internship_minor/', internship_minor, name='internship_minor'),
    path('internship_major/', internship_major, name='internship_major'),
    path('apply-internship/', apply_internship, name='apply_internship'),
]