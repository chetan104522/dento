from django.urls import path
from website import views

urlpatterns = [
    path('', views.index,name='index'),
    path('contact.html', views.contact,name='contact'),
    path('about.html', views.about,name='about'),
    path('service.html', views.service,name='service'),
    path('pricing.html', views.pricing,name='pricing'),
    path('blog-details.html', views.blog_details,name='blog-details'),
    path('blog.html', views.blog,name='blog'),
    path('appointment.html', views.appointment,name='appointment'),
]
