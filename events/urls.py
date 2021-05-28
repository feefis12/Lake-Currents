from django.urls import path
from . import views
from .views import Exclusive_Detail
from .views import Event_Detail


app_name = 'events'
urlpatterns = [
    path('today', views.home, name="home"),
    path('blog', views.blog, name="blog"),
    path('', views.fullWeek, name="full-week"),
    path('aboutUs', views.aboutUs, name="aboutUS"),
    path('register', views.register, name="register"),
    path('event-form',views.eventForm, name="event-form"),
    path('recent_video',views.Recentvideo,name="recent_video"),
    path('music-form', views.musicform, name="music-form"),
    path('discord-invite', views.discord,name='discord-invite'),
    path('full-blog', views.fullblog,name='full-blog'),
    path('blog/<slug>',Exclusive_Detail.as_view(), name='exclusive_blog'),
    path('diy-zone',views.diy, name="diy-zone"),
    path('contact', views.contact, name="contact"),
    path('<slug>', Event_Detail.as_view(),name='event_detail_view'),
 

]

