from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Event
from django.utils import timezone
import datetime
from .models import MostRecentVideo
from .forms import EmailList
from django.core.mail import send_mail, BadHeaderError
from .forms import Recieved_Events
from .forms import Recieved_Music
from .models import BlogPost
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import FavSongs
from .models import Discord
from .models import Exclusive
from .forms import Discord_Invite
# Create your views here.

# def all_events(request):
#
#     return render(request, "events/blog.html", {'event'})


class Event_Detail(DetailView):
    model = Event

    def get_context_data(self, **kwargs):
        context = super(Event_Detail,self).get_context_data(**kwargs)
        return context


class Exclusive_Detail(DetailView):
    model = Exclusive

    def get_context_data(self, **kwargs):
        context = super(Exclusive_Detail,self).get_context_data(**kwargs)
        return context

def exclusive_blog(request,slug):
    # post = get_object_or_404(Exclusive, slug=slug)
    return render(request, "events/exclusive_blog.html", {})

def event_detail(request,slug):
    return render(request, "events/event_detail.html", {})

def Recentvideo(request):
    vid = MostRecentVideo.objects.all()
    return render(request,'events/recent_video.html',{'vid': vid})

def diy(request):
    return render(request, "events/diy-zone.html", {})

def contact(request):
    return render(request, "events/contact.html", {})


def home(request):
    # event_list = Event.objects.all()
    # today = datetime.now()
    vid = MostRecentVideo.objects.all()
    event_list = Event.objects.all().filter(event_date__gte=timezone.now().replace(hour=0, minute=0, second=0), 
    event_date__lte=timezone.now().replace(hour=23, minute=59, second=59))
    return render(request,'events/index.html', {'event_list': event_list, 'vid':vid}, )

def fullWeek(request):
    # event_list = Event.objects.all()
    # today = datetime.now()
    event_list = Event.objects.all().order_by('event_date')
    return render(request,'events/full-week.html', {'event_list': event_list})

def eventForm(request):
    submitted= False
    if request.method == "POST":
        form=Recieved_Events(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/event-form?submitted=True')
    else:
        form = Recieved_Events
        if 'submitted' in request.GET:
            submitted=True


    form = Recieved_Events
    return render(request,'events/event-form.html',  {'form':form, 'submitted':submitted})



def blog(request):
   
    blog = BlogPost.objects.all()
    blog = BlogPost.objects.filter(published=True).order_by('-id')[:25]
    eBlog = Exclusive.objects.all()
    
    # blog = BlogPost.objects.order_by('-id')
    return render(request,'events/blog.html', {'blog': blog, 'eBlog': eBlog},)


def fullblog(request):
   
    blog = BlogPost.objects.all()
    blog = BlogPost.objects.filter(published=True).order_by('-id')
  
    
    # blog = BlogPost.objects.order_by('-id')
    return render(request,'events/full-blog.html', {'blog': blog})


def aboutUs(request):
    return render(request, "events/aboutUs.html", {})


def discord(request):
    if request.method == "GET":
        form = Discord_Invite
    else:
        form = Discord_Invite(request.POST)  
        if form.is_valid():   
            name = form['email'].value()
            email = form['email'].value()
            message = form['email'].value() + '\n' + form['music'].value()
              
            try:
                send_mail(name,message,email,['lakecurrents@gmail.com'])
                return HttpResponseRedirect('/discord-invite?submitted=True')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')  
    return render(request, "events/discord-invite.html", {'form': form,})
    

def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'events/register.html', {"form":form})

# def home(request):
#     submitted =  False
#     if request.method == "POST":
#         form=EmailList(request.POST)
#         if form.is_valid:
#             form.save()
#         return HttpResponseRedirect('/?submitted=True')    
#     else:
#         form = EmailList
#         if 'submitted' in request.GET:
#             submitted=True

#     form = EmailList    
#     return render(request,'events/home.html', {'form': form,'submitted' : submitted})

def musicform(request):
 
    if request.method == "GET":
        form = Recieved_Music
    else:
        form = Recieved_Music(request.POST)  
        if form.is_valid():   
            name = form['name'].value()
            email = form['email'].value()
            message = form['name'].value() + '\n' + form['email'].value() + '\n' +  form['release_date'].value() +'\n' + form['link'].value() +'\n' 
              
            try:
                send_mail(name,message,email,['lakecurrents@gmail.com'])
                return HttpResponseRedirect('/music-form?submitted=True')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, 'events/music-form.html', {'form': form})
           

            
            
   
    
