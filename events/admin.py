from django.contrib import admin
from .models import Event
from .models import FormEvent
from embed_video.admin import AdminVideoMixin
from .models import MostRecentVideo
from .models import BlogPost
from .models import Email
from .models import FavSongs
from .models import Exclusive

# class EventAdmin(admin.ModelAdmin):
#     exclude=('slug',)




@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name','event_date',)
    ordering = ('event_date',)
    search_fields = ('name','event_date',)
    exclude=('slug',)

@admin.register(FormEvent)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name','event_date',)
    ordering = ('event_date',)
    search_fields = ('name','event_date',)

@admin.register(MostRecentVideo)
class VideoAfmin(admin.ModelAdmin):
    list_display = ('name','vidlink')


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(BlogPost,)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','published', )
    exclude=('slug',)

@admin.register(Exclusive,)
class Exlusive(admin.ModelAdmin):
    list_display = ('name',)
    