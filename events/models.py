from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime, date


# class LAUSERS(models.Model):
#     username = models.CharField("User-Name",max_length=120)
#     email = models.EmailField("Emails")
#     def __str__(self):
#         return self.username



class Event(models.Model):
    CATEGORIES = (
    ("Show", "show"),
    ("Gallery", "gallery"),
    ("Bar", "bar"),
    ("Pop-up", "pop-up"),
    ("Other", "other"),
)
    name = models.CharField("Event Name", max_length=120)
    event_date= models.DateTimeField("Event Date")
    location = models.CharField("Event Location", max_length=120, blank=True)
    description = models.TextField("Event Description")
    fbLink = models.URLField("Social Media Link", blank=True)
    flyer = models.ImageField(upload_to="media/flyers", blank=True)
    slug = models.SlugField(max_length=200,unique=True, null=True)
    category = models.CharField('Category',  max_length=120, choices= CATEGORIES ,default="show")
    musicLinks = models.TextField("Bandcamp Link" , blank=True)
    # attending = models.ManyToManyField(LAUSERS, blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Event,self).save(*args, **kwargs)



# class Item(models.Model):
#     name = models.CharField('Video name', max_length=100, null=True)
#     video = EmbedVideoField(verbose_name="myVideo")  # same like models.URLField()
#     def __str__(self):
#         return self.name


class FormEvent(models.Model):
    name = models.CharField("Event Name", max_length=120)
    event_date= models.DateTimeField("Event Date")
    location = models.CharField("Event Location", max_length=120, blank=True)
    description = models.TextField("Event Description")
    fbLink = models.URLField("FB Link", blank=True)
    flyerLink = models.URLField("FlyerLink", blank=True)
    # attending = models.ManyToManyField(LAUSERS, blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(FormEvent,self).save(*args, **kwargs)

class MostRecentVideo(models.Model):
    name = models.CharField("Vid Name", max_length=120,default="")
    vidlink = models.URLField("Video Url", blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super(MostRecentVideo,self).save(*args, **kwargs)

class BlogPostQueryset(models.QuerySet):

    def published(self):
        return self.filter(published=True)
       
      

    def draft(self):
        return self.filter(published=False)



   


class BlogPost(models.Model):
    title = models.CharField("Post Title", max_length=120)
    cover = models.ImageField("Cover Art",upload_to="media/blog-Covers")
    body = models.TextField("Body")

    videoLink = models.URLField("Video Link")

    favSongTitle= models.CharField("Favorite Song 1", max_length=120,blank=True)
    favSongUrl= models.URLField("Song URL 1", max_length=120,blank=True)

    favSongTitle2= models.CharField("Favorite Song 2", max_length=120,blank=True)
    favSongUrl2= models.URLField("Song URL 2", max_length=120,blank=True)

    favSongTitle3= models.CharField("Favorite Song", max_length=120,blank=True, default=", ")
    favSongUrl3= models.URLField("Song URL 3", max_length=120,blank=True ,default=", ")
    
    page = models.CharField("Post ID", max_length=120,default="Band-Name")
    relatedArtist = models.CharField("Similar Artists",max_length=120,default="The Strokes", blank=True)
    instaLink = models.URLField("Insta URL" ,blank=True)
    twitterLink = models.URLField("Twitter URL" ,blank=True)
    bandcampLink = models.URLField("Bandcamp URL", blank=True)
    soundcloudLink = models.URLField("Soundcloud URL" ,blank=True)
    audiusLink = models.URLField("Audius URL" ,blank=True)
    published = models.BooleanField("published", default=False)
    objects = BlogPostQueryset.as_manager()

    def __str__(self):
        return self.title

   





class FavSongs(models.Model):
    name = models.CharField("Song name", max_length=120, blank=True)
    url = models.CharField("Timestamp", max_length=120,blank=True )
    songtag = models.OneToOneField(BlogPost ,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    



class MusicForm(models.Model):
    name= models.CharField("Artist Name", max_length=120)
    email= models.EmailField("Artist Email")
    release_date = models.DateTimeField("Release Date")
    link = models.URLField("Music Link", blank=True)
    description = models.TextField("Descripton", blank=True)


class Email(models.Model):
    email= models.EmailField("Email")

class Discord(models.Model):
    email = models.EmailField("Email")
    music = models.URLField("Music")

   


class Exclusive(models.Model):
    name = models.CharField("Post Title", max_length=120)
    cover = models.ImageField("Cover Art",upload_to="media/blog-Covers")
    body = models.TextField("Body")
    interviewer = models.TextField("Interviewer")
    videoLink = models.URLField("Video Link")

    favSongTitle= models.CharField("Favorite Song 1", max_length=120,blank=True)
    favSongUrl= models.URLField("Song URL 1", max_length=120,blank=True)

    favSongTitle2= models.CharField("Favorite Song 2", max_length=120,blank=True)
    favSongUrl2= models.URLField("Song URL 2", max_length=120,blank=True)

    favSongTitle3= models.CharField("Favorite Song", max_length=120,blank=True, default=", ")
    favSongUrl3= models.URLField("Song URL 3", max_length=120,blank=True ,default=", ")
    
    slug = models.SlugField(max_length=200,unique=True, null=True)
    published = models.BooleanField("published", default=False)
    objects = BlogPostQueryset.as_manager()

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Exclusive,self).save(*args, **kwargs)

    

