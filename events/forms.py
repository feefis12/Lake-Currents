from django import forms
from django.forms import ModelForm
from .models import FormEvent
from .models import MusicForm
from .models import Email
from .models import Discord

class Recieved_Events(ModelForm):
    class Meta:
        model = FormEvent
        fields = ('name', 'event_date', 'location', 'flyerLink', 'description', )
        labels={
            'name':'',
            'event_date' :'',
            'location':'',
            'description':'',
            'flyerLink':'',


        }
        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control ','placeholder':'Event Name','max-width':'10rem' } ),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Date'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Location'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'flyerLink':forms.TextInput(attrs={'class':'form-control','placeholder':'Image (Social Media Link)'}),

        }

class EmailList(ModelForm):
   class Meta:
        model = Email
        fields = ("email",)
        labels= {
            'email': '',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email','max-width':'20rem'} ),
        }




class Recieved_Music(ModelForm):
    class Meta:
        model = MusicForm
        fields = ('name', 'email', 'release_date', 'link', )
        labels={
            'name':'',
            'email' :'',
            'release_date':'',
            'link':'',
          
        }
        widgets = {

            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Artist Name','max-width':'20rem'} ),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'release_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Release Date'}),
            'link': forms.TextInput(attrs={'class':'form-control','placeholder':'Link'}),
            
        }


class Discord_Invite(ModelForm):
    class Meta:
        model = Discord
        fields = ("email", "music")
        labels= {
            'email': '',
            'music': '',
        }
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email','max-width':'20rem'} ),
            'music': forms.TextInput(attrs={'class':'form-control','placeholder':'Link to Music','max-width':'20rem'} ),
        }
